import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from uppgift4_program import Systembolaget

'# Call the setup fixture'
@pytest.mark.usefixtures("setup")
class TestSystembolaget:

    def test_login(self):
        email_field = self.driver.find_element(By.ID, "email-input")
        email_field.send_keys("Grupp.1.Python@gmail.com")
        password_field = self.driver.find_element(By.NAME, "Password")
        password_field.send_keys("Grupp1Python")
        login_button = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary button-submit']")
        login_button.click()

    def test_demo(self):
        sku1 = Systembolaget(self.driver)
        sku1.find_item("2722")
        demoartikel = self.driver.find_element(By.XPATH, "//div[@class='css-8zpafe e3whs8q0']//p[@class='css-12l74ml er6ap680']")
        demoartikel = demoartikel.text
        assert "2722" in demoartikel


