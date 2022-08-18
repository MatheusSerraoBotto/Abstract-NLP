

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from enviroment import enviroment
from build_query import build_query
from themes import themes 
import pandas as pd
import os

# Setting url
URL = enviroment['url']

# Setting constants selenium
TIME_TO_LOAD = enviroment['selenium']['time_to_load']
CLASS_NAME = enviroment['selenium']['class_name']
HEADLESS = enviroment['selenium']['headless']

# Setting constants query
START_YEAR = enviroment['query']['start_year']
END_YEAR = enviroment['query']['end_year']
PER_PAGE = enviroment['query']['per_page']


def create_csv_of_ids(theme: str, pages: int):
    try:
        # Setting options to WebDriverChrome
        options = Options()
        options.headless = HEADLESS

        # Starting WebDriver
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        
        results = []
        for page in range(1, pages+1):
            attempts = 0
            page_read = False
            while not page_read:
                try:
                    driver.get(build_query(URL, theme, (START_YEAR, END_YEAR), page, PER_PAGE))

                    # Waiting some elements to start scrapy
                    element_present = EC.presence_of_all_elements_located(
                        (By.CLASS_NAME, CLASS_NAME))
                    elements = WebDriverWait(driver, TIME_TO_LOAD).until(element_present)

                    # Waiting some elements to start scrap
                    content = driver.page_source
                    soup = BeautifulSoup(content, features="html.parser")

                    for a in soup.findAll('div', attrs={'class': CLASS_NAME}):
                        results.append(a.attrs['id'])
                    
                    page_read = True
                except:
                    attempts = attempts + 1
                    if attempts == 3:
                        break
        df = pd.DataFrame({'id': results})
        csv_name = theme.lower().replace(' ','_')
        filename = f'{csv_name}.csv'
        df.to_csv(os.path.join('code\WebScrap\src\ids', filename), index=False, encoding='utf-8')

    finally:
        driver.quit()

def generate_csv_of_themes():
    for theme in themes:
        theme_name = theme[0].lower().replace(' ','_')
        pages = theme[1]
        create_csv_of_ids(theme_name, pages)

generate_csv_of_themes()