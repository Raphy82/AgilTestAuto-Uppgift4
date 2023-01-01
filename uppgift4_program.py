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

    '#Find item on the website, open product page'
    def find_item(self, skus):
        sku = self.driver.find_element(By.XPATH, "//input[@placeholder='Sök dryck, land, hållbart val...']")
        sku.send_keys(skus)
        sku.send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, "//p[@class='css-w9tb7l e3wog7r1']").click()

    '#From product page, add item to basket'
    def add_item(self, buts):
        self.driver.find_element(By.XPATH, "//*[@id='__next']/main/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[3]/button[2]").click()
        but = self.driver.find_element(By.XPATH, "//*[@id='modalId']/div/div/form/label/div/input")
        but.send_keys(buts)
        self.driver.find_element(By.XPATH, "//*[@id='react-autowhatever-1-section-0-item-0']/div/span/strong").click()

