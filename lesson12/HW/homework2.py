import json
import logging

logging.basicConfig(filename='hw2.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
json_files = ['localizations_en.json', 'localizations_ru.json', 'login.json', 'swagger.json']
for files in json_files:
    try:
        with open(files, mode='r', encoding='utf-8') as file:
            json.load(file)
    except json.JSONDecodeError as e:
        logging.error(f'Invalid file {files}: {e}')
