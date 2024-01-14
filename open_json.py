import json

def open_json_file():
    with open('operations.json', 'r') as file:
        operations = json.load(file)

    return operations
