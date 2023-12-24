import json
import os
from pyfzf.pyfzf import FzfPrompt
import requests

def check_api():
    # Ask for the API URL
    print("For API details, please visit: https://github.com/junioralive/spycli-api.")
    print("To use the API, follow this format:")
    print(" - For local: http://localhost:5000/ or http://[your-local-ip]:5000/")
    print(" - For cloud hosting: Enter the URL of your hosted API.")
    
    api_url = input("Please enter your API URL: ")
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()

        data = response.json()

        if data.get("spy-cli") == "online":
            print("spy-cli is online")
            return api_url
        else:
            print("[!] Please check your API")
            return
    except requests.RequestException as e:
        print("[!] Please check your API")
        print(f"An error occurred: {e}")
        return

def prompt_and_config(api_url):
    # Define platform choices
    platforms = {
        "Windows": "windows",
        "Linux": "linux",
        "Android": "android",
        "iPhone": "iphone",
        "MAC": "mac"
    }

    # Create an instance of FzfPrompt
    fzf = FzfPrompt()

    # Use fzf to let the user select a platform
    print("Please select your platform:")
    platform_selection = fzf.prompt(list(platforms.keys()))
    selected_platform = platforms[platform_selection[0]]  # Assuming one selection

    # Define the path to the configuration file, it should be in the same directory as this script
    config_dir = os.path.dirname(os.path.realpath(__file__))
    config_file = os.path.join(config_dir, 'config.json')

    # Save the configuration to the file
    config_data = {
        "api_url": api_url,
        "platform": selected_platform
    }
    with open(config_file, 'w') as file:
        json.dump(config_data, file, indent=4)

    print("Configuration saved successfully.")

def configure():
    getapiurl = check_api()
    if not getapiurl:
        return
    else:
        prompt_and_config(getapiurl)
        
if __name__ == "__main__":
    configure()