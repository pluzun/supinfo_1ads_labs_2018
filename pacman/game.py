import json


def import_map(map_name):
    with open('{name}.json'.format(name=map_name), 'r') as file:
        file_line = file.read()

    try:
        # Try to import the json file
        return json.loads(file_line)
    except json.decoder.JSONDecodeError as error:
        # The json file is uncorrect
        print('There is an issue with your JSON file!')
        print(error)
        return {}


print(import_map('map_1'))
