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
    def login_email(self):
        email_field = self.driver.find_element(By.ID, "email-input")
        email_field.send_keys("Grupp.1.Python@gmail.com")

    '#Login to the website, insert password'
    def login_passwd(self):
        password_field = self.driver.find_element(By.NAME, "Password")
        password_field.send_keys("Grupp1Python")

    '#Login to the website, click on login button'
    def login_button(self):
        login_button = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary button-submit']")
        login_button.click()

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

