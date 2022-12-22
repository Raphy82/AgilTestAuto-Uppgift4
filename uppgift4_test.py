import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from uppgift4_program import Systembolaget

'# Call the setup fixture'
@pytest.mark.usefixtures("setup")
class TestSystembolaget:

    def test_demo(self):
        sku1 = Systembolaget(self.driver)
        sku1.find_artikel("2722")
        demoartikel = self.driver.find_element(By.XPATH, "//div[@class='css-8zpafe e3whs8q0']//p[@class='css-12l74ml er6ap680']")
        demoartikel = demoartikel.text
        assert "2722" in demoartikel


