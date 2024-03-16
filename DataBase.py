import json
import os

DB_PATH = 'db'

def check_db_path() -> None:
    """Checks if database path exists and creates one if doesn't."""

    if not os.path.exists(os.path.join(os.getcwd(), DB_PATH)):
        os.mkdir(DB_PATH)

def read_from_db(class_name: str) -> dict:
    """Reads data from DataBase based on class name"""

    dbFilePath = os.path.join(os.getcwd(), DB_PATH, f'{class_name}.json')
    if os.path.exists(dbFilePath):
        dbFile = open(dbFilePath, 'r')
        data = json.load(dbFile)
        dbFile.close()
        return data
    return {}

def write_to_db(class_name: str, new_data: dict, update_method: str) -> None:
    """Writes new data, removes or updates old data to DataBase based on class_name and update_method
    
    Args:
        update_method choices: add, remove, update
    """
    
    old_data = read_from_db(class_name)
    new_keys = new_data.keys()

    if update_method == 'add' or update_method == 'update':
        for key in new_keys:
            old_data[key] = new_data[key]
    elif update_method == 'remove':
        for key in new_keys:
            old_data.pop(key)
    else:
        pass

    dbFilePath = os.path.join(os.getcwd(), DB_PATH, f'{class_name}.json')
    if os.path.exists(dbFilePath):
        json_object = json.dumps(old_data, indent=4)
        with open(dbFilePath, 'r') as dbFile:
            dbFile.write(json_object)
