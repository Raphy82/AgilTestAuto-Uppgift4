import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from uppgift4_program import Systembolaget

'# Call the setup fixture'
@pytest.mark.usefixtures("setup")
class TestSystembolaget:

    def test_email(self):
        login1 = Systembolaget(self.driver)
        login1.login_email("Grupp.1.Python@gmail.com")
        username = self.driver.find_element(By.NAME, "Username")
        username = username.text
        assert "Grupp.1.Python@gmail.com" in username

    def test_password(self):
        name1 = Systembolaget(self.driver)
        name1.login_passwd("Grupp1Python")
        password = self.driver.find_element(By.NAME, "Password")
        password = password.text
        assert "Grupp1Python" in password

    def test_demo(self):
        sku1 = Systembolaget(self.driver)
        sku1.find_item("2722")
        demoartikel = self.driver.find_element(By.XPATH, "//div[@class='css-8zpafe e3whs8q0']//p[@class='css-12l74ml er6ap680']")
        demoartikel = demoartikel.text
        assert "2722" in demoartikel


