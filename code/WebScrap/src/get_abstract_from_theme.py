

from fileinput import filename
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from themes import themes
from enviroment import enviroment
import pandas as pd
import os
import time

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
    loop = 0
    while(True):
        try:
            if loop == 5:
                return 'NA', 'NA'
            # Setting options to WebDriverChrome
            driver.get(ARTICLE_URL + str(id))

            # Waiting some elements to start scrap
            abstract_element = EC.presence_of_element_located(
                (By.CLASS_NAME, CLASS_NAME_ABSTRACT))
            abstract = WebDriverWait(driver, TIME_TO_LOAD).until(abstract_element)
            abstract_text = abstract.text[10:]       

            title_element = EC.presence_of_element_located(
                (By.CLASS_NAME, CLASS_NAME_TITLE))
            title = WebDriverWait(driver, TIME_TO_LOAD).until(title_element)
            title_text = title.text

            return title_text, abstract_text
        except Exception as e:
            print(e)
            loop += 1
            pass

def write_abstract_in_csv(csv_name):
    filename = f'{csv_name}.csv'
    filepath_read = os.path.join('code\WebScrap\src\ids',filename)
    filepath_write = os.path.join(filename)

    
    df = pd.read_csv(filepath_read, sep='\t')
    df["title"] = ""
    df["abstract"] = ""

    i = 0
    times = []
    for index, row in df.iterrows():
        start_time = time.time()
        title_text, abstract_text = get_abstract_from_theme(row.id)
        df.at[index, 'title'] = title_text
        df.at[index, 'abstract'] = abstract_text
        diff_time = time.time() - start_time
        print("--- %s seconds ---" % (diff_time))
        times.append(diff_time)
        i+=1
        if i == 30:
            break
    print(times)

    # df.to_csv(filepath_write, index=False, encoding='utf-8')

def write_abstract_of_themes():
    for theme in themes:
        theme_name = theme[0].lower().replace(' ','_')
        write_abstract_in_csv(theme_name)

write_abstract_of_themes()

driver.quit()