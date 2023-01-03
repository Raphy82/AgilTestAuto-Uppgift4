import pytest
import re
import requests
from uppgift4_program import Systembolaget
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


'# Call the setup fixture'
@pytest.mark.usefixtures("setup")
class TestSystembolaget:

    def test_email(self):
        login1 = Systembolaget(self.driver)
        login1.login_email("Grupp.1.Python@gmail.com")
        username = self.driver.find_element(By.ID, "email-input")
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

    def test_product_price(self):
        product_price = self.driver.find_element(By.XPATH, "//div[@class='css-1df247k e3whs8q0']").text

        # En 'Regular expression operations' används för att plocka ut endast priset
        price_match = re.search(r'\d+:\d+', product_price)
        # Kontrollera att matchningen inte är None
        assert price_match is not None
        # Plocka ut matchningen och konvertera till en float
        price = float(price_match.group().replace(':', '.'))
        assert price in [89.0, 118.67]

    def test_product_image_loads_correctly(self):
        image_element = self.driver.find_element(By.XPATH, "//img[@class='css-0 e53gfhp1']")
        image_src = image_element.get_attribute("src")
        response = requests.get(image_src)
        assert response.status_code == 200

    def test_add_wine_to_cart(self):
        ombud_button = self.driver.find_element(By.XPATH, "//div[@class='css-lioehz ewphso25']")
        ombud_button.click()
        # Wait for the postal code field to be visible
        ombud_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Sök ombud']"))
        )
        ombud_field.send_keys("lyrestad")

        valj_ombud_button = self.driver.find_element(By.XPATH, "//div[@class='false emejrsp0 css-1naf3kp e1uubc4q0']")
        valj_ombud_button.click()

        add_to_cart_button = self.driver.find_element(By.XPATH, "//button[@class='css-1fej1r5 ev9wvac0']")
        add_to_cart_button.click()

        cart_icon = self.driver.find_element(By.XPATH, "//p[@class='css-l7e9hy enp2lf70']")
        assert cart_icon.text == "1"

    def test_search_name(self):
        product = Systembolaget(self.driver)
        product.byname("Maison Sassy  Cidre Organic")
        name = self.driver.find_element(By.XPATH, " ")
        name = name.text
        print(name)
        assert "Maison Sassy  Cidre Organic" in name

    def test_search_product_nr(self):
        product = Systembolaget(self.driver)
        product.bynr("13023")
        articel = self.driver.find_element(By.XPATH, "//div[@class='css-8zpafe e3whs8q0']//p[@class='css-12l74ml er6ap680']")
        articel = articel.text
        print(articel)
        assert "13023" in articel

    def test_alcohol_content(self):
        alcohol = Systembolaget(self.driver)
        alcohol.content = ("4%")
        procent = self.driver.find_element(By.XPATH, "div[class ='css-1to8dtu e3whs8q0'] p:nth - child(3)")
        procent = procent.text
        print(procent)
        assert "4%" in procent

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

