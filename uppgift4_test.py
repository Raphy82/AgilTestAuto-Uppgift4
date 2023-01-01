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

    def test_product_nr(self):
        search_input = Systembolaget(self.driver)
        search_input.search_for_product("11903")
        product_nr = self.driver.find_element(By.XPATH, "//div[@class='css-8zpafe e3whs8q0']//p[@class='css-12l74ml er6ap680']").text
        assert "11903" in product_nr
    def test_product_name(self):
        product_name = self.driver.find_element(By.XPATH,
                                                "//div[@class='css-dahppd e3whs8q0']//p[@class='css-1rw23u7 enp2lf70']").text
        assert product_name == "Casa Emma"
    def test_demo(self):
        sku1 = Systembolaget(self.driver)
        sku1.find_item("11903")
        demoartikel = self.driver.find_element(By.XPATH, "//div[@class='css-8zpafe e3whs8q0']//p[@class='css-12l74ml er6ap680']")
        demoartikel = demoartikel.text
        assert "11903" in demoartikel



    def test_cart(self):
        self.driver.find_element(By.XPATH, "//body/div[@id='__next']/header/div/div/div/div/div/button[1]").click()
        vin = self.driver.find_element(By.XPATH, "//*[@id='__next']/header/div/div/div/div[2]/div[5]/div/div/div[2]/div[1]/div/div/div[2]/div/div[1]/a/div/h3/span[1]")
        vin = vin.text
        assert "Casa Emma" in vin

        vin_pris = self.driver.find_element(By.XPATH, "//span[normalize-space()='89:-']")
        vin_pris = vin_pris.text
        assert "89" in vin_pris

        cider = self.driver.find_element(By.XPATH, "//span[normalize-space()='Maison Sassy']")
        cider = cider.text
        assert "Maison Sassy" in cider

        cider_pris = self.driver.find_element(By.XPATH, "//span[normalize-space()='21:90*']")
        cider_pris = cider_pris.text
        assert "21:90" in cider_pris

        pant = self.driver.find_element(By.XPATH, "//p[normalize-space()='1:-']")
        pant = pant.text
        assert "1" in pant

        tot_pris = self.driver.find_element(By.XPATH, "//p[normalize-space()='111:90']")
        tot_pris = tot_pris.text
        assert "111:90" in tot_pris

