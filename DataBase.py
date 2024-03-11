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
        dbFile = open(dbFilePath)
        data = json.load(dbFile)
        dbFile.close()
        return data
    return {}
