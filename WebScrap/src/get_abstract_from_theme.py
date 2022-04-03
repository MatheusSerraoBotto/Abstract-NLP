

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from themes import themes
from enviroment import enviroment
import pandas as pd

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

def get_abstract_from_theme(id: str):
    while(True):
        try:
            # Setting options to WebDriverChrome
            driver.get(ARTICLE_URL + str(id))

            # Waiting some elements to start scrap
            abstract_element = EC.presence_of_all_elements_located(
                (By.CLASS_NAME, CLASS_NAME_ABSTRACT))
            abstract = WebDriverWait(driver, TIME_TO_LOAD).until(abstract_element)
            abstract_text = abstract[0].text[10:]       

            title_element = EC.presence_of_all_elements_located(
                (By.CLASS_NAME, CLASS_NAME_TITLE))
            title = WebDriverWait(driver, TIME_TO_LOAD).until(title_element)
            title_text = title[0].text

            return title_text, abstract_text
        except:
            pass

def write_abstract_in_csv(csv_name):
    filepath = f'./themes/{csv_name}.csv'
    
    df = pd.read_csv(filepath, sep='\t')
    df["title"] = ""
    df["abstract"] = ""

    for index, row in df.iterrows():
        title_text, abstract_text = get_abstract_from_theme(row.id)
        df.at[index, 'title'] = title_text
        df.at[index, 'abstract'] = abstract_text
        print(row)

    df.to_csv(filepath, index=False)

def write_abstract_of_themes():
    for theme in themes:
        theme = theme.lower().replace(' ','_')
        write_abstract_in_csv(theme)

write_abstract_of_themes()

driver.quit()