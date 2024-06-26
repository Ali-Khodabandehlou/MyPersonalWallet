import json
import os

DB_PATH = 'db'

def check_db_path() -> None:
    """Checks if database path exists and creates one if doesn't."""

    if not os.path.exists(os.path.join(os.getcwd(), DB_PATH)):
        os.mkdir(DB_PATH)

def last_pk(data: dict) -> int:
    """returns last pk of object"""
    keys = sorted(data.keys())
    if len(keys):
        return int(keys[-1])
    return 0

def read_from_db(class_name: str) -> dict:
    """Reads data from DataBase based on class name"""

    check_db_path()
    dbFilePath = os.path.join(os.getcwd(), DB_PATH, f'{class_name}.json')
    if os.path.exists(dbFilePath):
        dbFile = open(dbFilePath, 'r')
        data = json.load(dbFile)
        dbFile.close()
        return data
    return {}

def write_to_db(class_name: str, new_data: dict, write_method: str, pk: int = None) -> bool:
    """Writes new data, removes or updates old data to DataBase based on class_name and update_method
    
    Args:
        write_method choices: add, remove, update

    Retuen:
        False if error
        True if OK
    """
    
    old_data = read_from_db(class_name)

    if write_method == 'add':  # Create method
        new_pk = last_pk(old_data) + 1
        old_data[str(new_pk)] = new_data
    elif write_method == 'update':  # Update method
        if not pk:
            return False
        if str(pk) not in old_data.keys():
            return False
        old_data[str(pk)] = new_data
    elif write_method == 'remove':  # Remove method
        old_data.pop(str(pk))
    else:
        return False
    
    # write to DB
    check_db_path()
    dbFilePath = os.path.join(os.getcwd(), DB_PATH, f'{class_name}.json')
    json_object = json.dumps(old_data, indent=4)
    with open(dbFilePath, 'w') as dbFile:
        dbFile.write(json_object)
    return True
