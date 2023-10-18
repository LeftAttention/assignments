import configparser
import json
from flask import Flask, jsonify

app = Flask(__name__)

# Initialize a dictionary to store the configuration data
config_data = {}

def read_config_file(file_path):
    """
    Read the config file and dispay the config data in browser (http://127.0.0.1:5000/get_config).

    Parameters:
        file_path (str): Path of the config file in .ini format
    """
    config = configparser.ConfigParser()
    try:
        config.read(file_path)
        
        for section in config.sections():
            config_data[section] = {}
            for key in config[section]:
                config_data[section][key] = config[section][key]
                
        # Save the dictionary as a JSON file
        with open('config_data.json', 'w') as f:
            json.dump(config_data, f)
            
    except FileNotFoundError:
        print("Configuration file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to read the config file
read_config_file('sample_config.ini')

# Flask GET API to fetch the configuration data
@app.route('/get_config', methods=['GET'])
def get_config():
    return jsonify(config_data)

if __name__ == "__main__":
    app.run(debug=True)
