

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
PAGES = enviroment['query']['pages']


def create_csv_of_ids(theme: str):
    try:
        # Setting options to WebDriverChrome
        options = Options()
        options.headless = HEADLESS

        # Starting WebDriver
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        
        results = []
        for page in range(1, PAGES+1):
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

        df = pd.DataFrame({'id': results})
        df.to_csv(f"themes/{theme.lower().replace(' ','_')}.csv", index=False, encoding='utf-8')

    finally:
        driver.quit()

def generate_csv_of_themes():
    for theme in themes:
        create_csv_of_ids(theme)

generate_csv_of_themes()