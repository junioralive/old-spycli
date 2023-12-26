import requests
import json
from pyfzf.pyfzf import FzfPrompt
from spy_cli.util.scrapper import vid_parser_m

# -----------------------------
# REQUEST AND FETCH
# -----------------------------

# Search and fetch movie/tv
def fetch_and_format_tmdb_data(query):
    # API endpoint and headers
    url = f"https://api.themoviedb.org/3/search/multi?query={query}"
    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYWRlOWFjMmM3ZjRiZGE4NDc4OWIzZTFjMjUyMWI2NSIsInN1YiI6IjY1MmI1ZmMxMDI0ZWM4MDEwMTUxZGM5YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.l66sbxDcyEBslvFQoSfmsqvupaCvHORm1ie6giOGBaY"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        results_dict = {}
        for item in data["results"]:
            # Get 'name' or 'title'
            name_or_title = item.get('name', item.get('title', 'Unknown'))

            # Get 'origin_country'
            origin_country = ', '.join(item.get('origin_country', ['Unknown']))

            # Combine name/title and origin_country
            combined_name = f"{name_or_title} - {origin_country}"

            # Assigning the combined string with the link
            link = f"https://api.themoviedb.org/3/{item['media_type']}/{item['id']}"
            results_dict[combined_name] = link

        return json.dumps(results_dict, indent=4)
    else:
        return f"Failed to fetch data: {response.status_code}"
    
# Fetch movie/tv details
def get_seasons_episode_structure(url):
    # API endpoint and headers
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYWRlOWFjMmM3ZjRiZGE4NDc4OWIzZTFjMjUyMWI2NSIsInN1YiI6IjY1MmI1ZmMxMDI0ZWM4MDEwMTUxZGM5YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.l66sbxDcyEBslvFQoSfmsqvupaCvHORm1ie6giOGBaY"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return f"Failed to fetch data: {response.status_code}"

    data = response.json()
    seasons_data = data.get('seasons', [])

    seasons_episode_structure = {}
    for season in seasons_data:
        if season['name'].lower() != 'specials' and season['episode_count'] > 0:
            season_name = season['name']
            episode_count = season['episode_count']
            episodes = [f'Episode {i+1}' for i in range(episode_count)]
            seasons_episode_structure[season_name] = episodes

    return seasons_episode_structure,url

# -----------------------------
# DISPLAY AND PROMPTS
# -----------------------------


# Function to display prompt for search
def display_and_choose_options(json_data):
    data = json.loads(json_data)
    fzf = FzfPrompt()
    options = list(data.keys())  # Display only the keys (titles)
    result = fzf.prompt(options, "--cycle")
    selected_key = result[0] if result else None
    if selected_key:
        return data[selected_key]
    else:
        print("No selection made.")
        
# Function to display prompt for TV details
def select_season_and_episode(seasons_episodes):
    fzf = FzfPrompt()

    while True:
        # Select season
        seasons = list(seasons_episodes.keys())
        selected_season = fzf.prompt(seasons, "--cycle")[0]

        while True:
            # Prepare episodes list with 'back' as the first option
            episodes = ['back'] + seasons_episodes[selected_season]

            # Prompt user to select an episode or go back
            selected_episode_str = fzf.prompt(episodes, "--cycle")[0]

            # Check if user chose 'back' option
            if selected_episode_str == 'back':
                break  # Breaks the inner loop, returns to season selection

            selected_episode = int(selected_episode_str.split(' ')[-1])  # Extract only the episode number
            return selected_season, selected_episode

# -----------------------------
# UTILS
# -----------------------------

#CHECK if url is movie/tv
def check_url_type(url):
    if "tv" in url:
        streamlink = format_series_link(url)
        return streamlink
    elif "movie" in url:
        streamlink = format_movie_link(url)
        return streamlink
    else:
        return "Invalid Link"
    
#Formatting tv url
def format_series_link(apiurl):
    seasons_episodes, url = get_seasons_episode_structure(apiurl)
    if isinstance(seasons_episodes, dict):
        season, episode = select_season_and_episode(seasons_episodes)
        formatseason = season.replace("Season ","")
        formaturl = url.replace("https://api.themoviedb.org/3","https://vidsrc.to/embed")
        formatted_url = f"{formaturl}/{formatseason}/{episode}"
        return formatted_url
    else:
        print("[!] Something went wrong!")
        return None
    
#Formatting movie url
def format_movie_link(apiurl):
    if isinstance(apiurl, str):
        formaturl = apiurl.replace("https://api.themoviedb.org/3", "https://vidsrc.to/embed")
        return formaturl
    else:
        print("[!] Invalid input. 'apiurl' should be a string.")
        return None
        
        
# -----------------------------
# MAIN FUNCTION
# -----------------------------

def spyclinsm():
    while True:
        print("You'r using no-server version.")
        print("For more details, please visit: https://github.com/junioralive/spycli-noserver.")
        query = input("\033[94mEnter Search: \033[0m")

        if not query:
            print("Please enter a valid name.")
            continue

        formatted_json = fetch_and_format_tmdb_data(query)
        if formatted_json.startswith("Failed"):
            print(formatted_json)  # Display error message
            continue

        getlink = display_and_choose_options(formatted_json)
        if not getlink:
            print("No selection made or no results found.")
            continue

        streaminglink = check_url_type(getlink)
        vid_parser_m(streaminglink)

if __name__ == "__main__":
    spyclinsm()