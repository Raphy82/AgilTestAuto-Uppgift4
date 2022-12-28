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

    '#Click on logga in button on the upper right corner'
    def login_box(self):
        login_box = self.driver.find_element(By.XPATH, "//button[normalize-space()='Logga in']")
        login_box.click()

    '#Login to the website, insert email'
    def login_email(self):
        logins = self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Grupp.1.Python@gmail.com")
        logins.send_keys(Keys.ENTER)

    '#Find item on the website'
    def find_item(self, skus):
        sku = self.driver.find_element(By.XPATH, "//input[@placeholder='Sök dryck, land, hållbart val...']")
        sku.send_keys(skus)
        sku.send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, "//p[@class='css-w9tb7l e3wog7r1']")
        sku.click()

    '#From product page, add item to basket'
    def add_item(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Lägg i varukorg']").click()

