from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from .utils import type_and_enter

def website(driver, company_name, url, xpath):
    '''
    Open a website with Selenium
    '''
    driver.get(url)
    input_box = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    type_and_enter(input_box, company_name)
    return None

