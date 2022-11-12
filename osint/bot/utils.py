from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def initiate_bot():
    '''
    Set up a Selenium bot
    '''
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver

def type_and_enter(input_box, company_name):
    '''
    Type the company name in a search box and hit enter
    '''
    input_box.send_keys(company_name)
    input_box.send_keys(Keys.RETURN)
    return None