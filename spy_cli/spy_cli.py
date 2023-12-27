import requests
from requests.exceptions import ConnectionError, RequestException
from pyfzf.pyfzf import FzfPrompt
import subprocess
import time
try:
    from spy_cli.util.config import get_config
except FileNotFoundError:
    print("Configuration file not found. Please run 'spy-cli.config' to generate it.")
    exit(1)

def search():
    # Access the configuration
    config = get_config()
    # Extract configuration values
    api_url = config.get('api_url')
    
    try:
        # Prompt for input with sky blue color
        search = input("\033[94mEnter Search: \033[0m")
        # API URL
        api_url = f'{api_url}search?query={search}'
        # Making a GET request to the Flask API
        response = requests.get(api_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            searchresults = response.json()
            return searchresults
        else:
            print("Error: Received non-200 status code from API.")
            
    except ConnectionError:
        # Handle the ConnectionError specifically
        print("An error occurred: Failed to establish a new connection with the API.")
        print("Please check your API, try spycli.config to change your API.")
        
    except RequestException as e:
        # Handle any exceptions that occur during the HTTP request
        print(f"An error occurred: {e}")
        
    except Exception as e:
        # Handle other exceptions
        print(f"An unexpected error occurred: {e}")
    
def display_and_select(movies):
    if not movies:
        print("No movies available.")
        return None
    fzf = FzfPrompt()
    # Create a list of strings for each movie
    movies_list = [f"{index}. {movie['title']}" for index, movie in enumerate(movies, 1)]
    # Get the selected movie string
    selected_string = fzf.prompt(movies_list)[0]
    selected_index = selected_string.split('.')[0]
    # Convert the index back to integer and get the selected movie
    selected_movie = movies[int(selected_index) - 1]
    return selected_movie['link']

def fetch_links(url):
    # Access the configuration
    config = get_config()
    # Extract configuration values
    api_url = config.get('api_url')    
    try:
        # API URL
        api_url = f'{api_url}fetch?url={url}'
        # Making a GET request to the Flask API
        response = requests.get(api_url)
        # Check if the request was successful
        if response.status_code == 200:
            searchresults = response.json()
            return searchresults
        else:
            print("Error: Received non-200 status code from API.")
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the HTTP request
        print(f"An error occurred during the request: {e}")
    except Exception as e:
        # Handle other exceptions
        print(f"An unexpected error occurred: {e}")

# Function to prompt movies
def movies_display_prompt(movie_dict):
    fzf = FzfPrompt()
    if not movie_dict:
        print("No movies available.")
        return None
    # Create a list of movie titles
    titles = list(movie_dict.keys())
    # Use pyfzf to interactively select a title
    selected_title = fzf.prompt(titles)
    if not selected_title:
        return None
    selected_title = selected_title[0]  # Get the selected title
    # Print the selected movie's URL
    #print(f"Selected: {selected_title}")
    #print(f"URL: {movie_dict[selected_title]}")
    return movie_dict[selected_title]

# Function to prompt web series 
def series_display_prompt(data, selecting_season=True, selected_season=None):
    fzf = FzfPrompt()
    if selecting_season:
        # Create a list of season and resolution options, including a 'Back' option
        seasons_and_resolutions = ["Back"] + list(data.keys())
        selected_season_resolution = fzf.prompt(seasons_and_resolutions)[0]
        # Handle the 'Back' selection or recursion termination
        if selected_season_resolution == "Back":
            print("Loading...")
            return None
        # Recursive call to select an episode
        return series_display_prompt(data, selecting_season=False, selected_season=selected_season_resolution)
    else:
        # Create a list of episodes for the selected season and resolution
        episodes = ["Back"] + list(data[selected_season].keys())
        selected_episode = fzf.prompt(episodes)[0]
        if selected_episode == "Back":
            # Recursive call to go back to season selection
            return series_display_prompt(data, selecting_season=True)
        # Get and return the first link of the selected episode
        first_link = data[selected_season][selected_episode][0]
        return first_link

def display_and_stream(parsed_content):
    data = parsed_content['data']
    typecheck = parsed_content['type']

    if typecheck == 'series':
        return series_display_prompt(data)
    elif typecheck == 'movie':
        return movies_display_prompt(data)
    else:
        print("[!] Something went wrong.")

def scrape_streaminglink(url):
    # Access the configuration
    config = get_config()
    # Extract configuration values
    api_url = config.get('api_url')
    try:
        # API URL
        api_url = f'{api_url}scrape?url={url}'
        # Making a GET request to the Flask API
        response = requests.get(api_url)
        # Check if the request was successful
        if response.status_code == 200:
            searchresults = response.json()
            # Ensure that the 'stream' key is in the response
            if 'stream' in searchresults:
                return searchresults['stream']
            else:
                print("Error: 'stream' key not found in the response.")
        else:
            print("Error: Received non-200 status code from API.")
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that occur during the HTTP request
        print(f"An error occurred during the request: {e}")
    except Exception as e:
        # Handle other exceptions
        print(f"An unexpected error occurred: {e}")

#FUNCTION TO PLAY        
def ply(initial_url):
    # Access the configuration
    config = get_config()
    # Extract configuration values
    platform = config.get('platform')

    url = initial_url
    referrer = 'http://spymovies.com'  # Default referrer
    media_title = 'SPY Movies'  # Default media title
    
    try:
        if platform == 'windows':
            mpv_path = r"C:\mpv\mpv.exe"
            subprocess.Popen([mpv_path, f"--referrer={referrer}", url, f"--force-media-title={media_title}"])
            print("Playing, please wait...")
            time.sleep(5)
            
        elif platform == 'linux':
            try:
                subprocess.Popen(["mpv", f"--referrer={referrer}", url, f"--force-media-title={media_title}"], shell=False)
                print("Playing, please wait...")
                time.sleep(5)
            except Exception as e:
                print(f"Error occurred: {e}")
            
        elif platform == 'android':
            subprocess.Popen(["am", "start", "-n", "is.xyz.mpv/is.xyz.mpv.MPVActivity", "-e", "filepath", url])
            print("Playing, please wait...")
            time.sleep(5)
            
        elif platform == 'iphone':
            print(f"\033]8;;vlc://{url}\033\\-------------------------\n- Tap to open -\n-------------------------\033]8;;\033\\\n")
            input("Press Enter to continue...")
            
        elif platform == 'mac':
            subprocess.Popen(["iina", "--no-stdin", "--keep-running", f"--mpv-referrer={referrer}", url, f"--mpv-force-media-title={media_title}"])
            print("Playing, please wait...")
            time.sleep(5)
        else:
            print("[!] Please install player.")
    except Exception as e:
            print("[!] Error occurred:", e)
            
    # Initialize FzfPrompt
    fzf = FzfPrompt()
    
        # Commands for different media players, plus Exit and Search options
    commands = {
        "Download":None,
        "Search": None,
        "quit": None
    }

    while True:
        # Ask the user to select an option
        choice = fzf.prompt(list(commands.keys()), "--cycle")[0]

        # Check for exit condition
        if choice == "quit":
            print("Quiting spy-cli...")
            break

        # Handle the Search option
        if choice == "Search":
            spym_cli()
            
        if choice == "Download":
            print(f"\033]8;;{url}\033\\-------------------------\n- Tap to download -\n-------------------------\033]8;;\033\\\n")
            input("Press Enter to continue...")
        
#MAIN FUNCTION
def spym_cli():
    movies_list = search()
    if not movies_list:
        print("[!] Oops, not found.")
        print("[!] Try using spy-cli-basic, it might work.")
        return spym_cli()
    selected_movie = display_and_select(movies_list)
    if not selected_movie:
        print("[!] Oops, no links found.")
        return
    streaming_link = fetch_links(selected_movie)
    if not streaming_link:
        print("[!] Oopss, no streaming links found.")
        return
    streamme = display_and_stream(streaming_link)
    if not streamme:
        print("[!] Oops, search again.")
        return
    if streamme.startswith('https://hubcloud.lol/video/'):
        play_link = scrape_streaminglink(streamme)
        ply(play_link)
    else:
        print("[!] This link is not supported.")
        print(f"\033]8;;{streamme}\033\\-------------------------\n- Tap to download -\n-------------------------\033]8;;\033\\\n")
        input("Press Enter to continue...")
        spym_cli()
    
if __name__ == "__main__":
    spym_cli