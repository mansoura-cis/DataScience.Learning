from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ex 
from selenium.webdriver.common.by import By


class Covid19Extractor:
    ChromeOptions = Options()
    URL = 'https://www.worldometers.info/coronavirus/'

    def __init__(self):
        self.ChromeOptions.add_argument('--headless')
        driver = webdriver.Chrome(options = self.ChromeOptions)
        driver.get(self.URL)
    
    def getDataTable():
        pass
        



