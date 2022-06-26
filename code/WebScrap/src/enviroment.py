from dotenv import load_dotenv
import os

load_dotenv() 

enviroment = {
    'url': os.environ['URL'],
    'article_url': os.environ['ARTICLES_URL'],
    'selenium': {
        'headless': eval(os.environ['HEADLESS']),
        'time_to_load': int(os.environ['TIME_TO_LOAD']),
        'class_name': os.environ['CLASS_NAME'],
        'class_name_abstract': os.environ['CLASS_NAME_ABSTRACT'],
        'class_name_title': os.environ['CLASS_NAME_TITLE']
    },
    'query': {
        'start_year': int(os.environ['START_YEAR']),
        'end_year': int(os.environ['END_YEAR']),
        'per_page': int(os.environ['PER_PAGE']),
        'pages': int(os.environ['PAGES'])
    }    
}