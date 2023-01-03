import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

'# Call the setup fixture'
@pytest.mark.usefixtures("setup")
class Systembolaget:
    def __init__(self, driver):
        self.driver = driver

    '#Login to the website, insert email'
    def login_email(self, logins):
        login = self.driver.find_element(By.NAME, "Username")
        login.send_keys(logins)
        login.send_keys(Keys.ENTER)

    '#Login to the website, insert password + click on login button'
    def login_passwd(self, names):
        name = self.driver.find_element(By.NAME, "Password")
        name.send_keys(names)
        name.send_keys(Keys.ENTER)

    '#Find item on the website & open product page'
    def search_for_product(self, search):
        search_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Sök dryck, land, hållbart val...']")
        search_input.send_keys(search)
        time.sleep(2)
        search_input.send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, "//p[@class='css-w9tb7l e3wog7r1']").click()
