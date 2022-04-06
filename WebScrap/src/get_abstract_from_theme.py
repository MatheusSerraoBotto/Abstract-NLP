

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from themes import themes
from enviroment import enviroment
import pandas as pd
from bs4 import BeautifulSoup

# Setting url
ARTICLE_URL = enviroment['article_url']

# Setting constants selenium
TIME_TO_LOAD = enviroment['selenium']['time_to_load']
CLASS_NAME_ABSTRACT = enviroment['selenium']['class_name_abstract']
CLASS_NAME_TITLE = enviroment['selenium']['class_name_title']
HEADLESS = enviroment['selenium']['headless']

options = Options()
options.headless = HEADLESS

# Starting WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

def get_abstract_from_theme(url: str):
    while(True):
        try:
            # Setting options to WebDriverChrome
            driver.get(url)

            # Waiting some elements to start scrap
            abstract_element = EC.presence_of_element_located(
                (By.CLASS_NAME, CLASS_NAME_ABSTRACT))
            abstract = WebDriverWait(driver, TIME_TO_LOAD).until(abstract_element)

            content = driver.page_source
            soup = BeautifulSoup(content, features="html.parser")

            a = soup.findAll('div', attrs={'class': CLASS_NAME_ABSTRACT})[0]
            return a.contents[2].text, a.contents[8].text
        except:
            pass

def write_abstract_in_csv(csv_name):
    import json
    f = open('/home/mserrao/Documentos/TCC_V2/WebScrap/JSON/response.json')
    data = json.load(f)
    results = data['Articles']
    data = {'title': [], 'abstract': []}
    for article in results:
        title_text, abstract_text = get_abstract_from_theme(article['PublicUrl'])
        data['title'].append(title_text) 
        data['abstract'].append(abstract_text) 
    df = pd.DataFrame.from_dict(data)
    df.to_csv('/home/mserrao/Documentos/TCC_V2/WebScrap/src/themes/anxiety.csv', index=False)

def write_abstract_of_themes():
    for theme in themes:
        theme = theme.lower().replace(' ','_')
        write_abstract_in_csv(theme)

write_abstract_of_themes()

driver.quit()