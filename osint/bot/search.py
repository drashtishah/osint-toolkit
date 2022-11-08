from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from .constants import *
from .utils import *

def open_corporates(driver, company_name):
    driver.get(OPEN_CORP_URL)
    input_box = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, open_corporates_search_box)))
    type_and_enter(input_box, company_name)
    return None

def sec(driver, company_name):
    driver.get(SEC_URL)
    input_box = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, sec_search_box)))
    type_and_enter(input_box, company_name)
    return None

