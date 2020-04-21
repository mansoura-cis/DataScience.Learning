from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ex 
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


def getDataTable():
    ChromeOptions = Options()
    ChromeOptions.add_argument('--headless')
    driver = webdriver.Chrome(options = ChromeOptions)
    driver.get('https://www.worldometers.info/coronavirus/')
    PGsrc = driver.page_source
    PageSrc = BeautifulSoup( PGsrc , "lxml")
    HtmlTable =PageSrc.find(id ='main_table_countries_today')
    return HtmlTable
        



