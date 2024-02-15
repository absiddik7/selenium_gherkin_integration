from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from environment import BROWSER

def setup_driver(browser = BROWSER):
    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception(f"Browser '{browser}' is not supported")
    return driver


def teardown_driver(driver):
    driver.quit()