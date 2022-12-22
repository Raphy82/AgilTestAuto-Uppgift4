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

    '#Find item on the website'
    def find_item(self, skus):
        sku = self.driver.find_element(By.XPATH, "//input[@placeholder='Sök dryck, land, hållbart val...']")
        sku.send_keys(skus)
        sku.send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, "//p[@class='css-w9tb7l e3wog7r1']").click()

    '#From product page, add item to basket'
    def add_item(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Lägg i varukorg']").click()

