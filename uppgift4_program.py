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

    '#Login to the website, insert password'
    def login_passwd(self, names):
        name = self.driver.find_element(By.NAME, "Password")
        name.send_keys(names)
        name.send_keys(Keys.ENTER)

    '#Login to the website, click on login button'
    def login_button(self):
        checkbox = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary button-submit']")
        checkbox.click()

    '#Click on "Sofia"'
    def user_button(self):
        self.driver.find_element(By.XPATH, "//*[contains(text(), 'Sofia')]").click()

    '#Logout from website'
    def logout_button(self):
        self.driver.find_element(By.XPATH, "//button[@//*[@id='__next']/header/div/div/div/div[2]/div[2]/div/a[7]/p]").click()

    '#Find item on the website & open product page'
    def search_for_product(self, search):
        search_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Sök dryck, land, hållbart val...']")
        search_input.send_keys(search)
        time.sleep(2)
        search_input.send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, "//p[@class='css-w9tb7l e3wog7r1']").click()

    '#From product page, add item to basket'
    def add_item(self, buts):
        self.driver.find_element(By.XPATH, "//*[@id='__next']/main/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[3]/button[2]").click()
        but = self.driver.find_element(By.XPATH, "//*[@id='modalId']/div/div/form/label/div/input")
        but.send_keys(buts)
        self.driver.find_element(By.XPATH, "//*[@id='react-autowhatever-1-section-0-item-0']/div/span/strong").click()

