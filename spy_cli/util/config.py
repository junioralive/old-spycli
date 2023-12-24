# spy_cli/util/config.py

import json
import os

# Define the path to the configuration file relative to this file
config_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.json')

# Initialize a variable to hold the configuration
configuration = {}

def load_configuration():
    """ Load the configuration from the config.json file. """
    if os.path.exists(config_file_path):
        with open(config_file_path, 'r') as file:
            global configuration
            configuration = json.load(file)
    else:
        raise FileNotFoundError("Configuration file not found. Please run 'spy-cli.config' to generate it.")

# Attempt to load the configuration when the module is imported
load_configuration()

def get_config():
    """ Accessor method for the configuration """
    return configuration
