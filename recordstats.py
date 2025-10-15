import json
import os


FILE_PATH = "playerstats.json"
DEFAULT_DATA = {"p_score": 0, "value": 1}


def load_stats():
    if os.path.exists(FILE_PATH):
        try:
            with open(FILE_PATH, "r") as file:
                data = json.load(file)
                
                # Ensure data is a dict
                if isinstance(data, dict):
                    for key, value in DEFAULT_DATA.items():
                        data.setdefault(key, value)
                    return data
                else:
                    # Unexpected data type — treat as corrupted
                    print("Invalid data format (not a dict), using defaults.")
        except (json.JSONDecodeError, ValueError, IOError) as e:
            print(f"Error reading JSON file: {e}")

    # If file doesn't exist or is bad, return defaults
    return DEFAULT_DATA.copy()
    
def save_stats(data):
    """Save the current stats to a JSON file."""
    with open(FILE_PATH, "w") as file:
        json.dump(data, file) #serializes(converts) data into json readable

