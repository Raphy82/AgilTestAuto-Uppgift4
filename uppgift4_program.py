from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.systembolaget.se")
driver.fullscreen_window()
time.sleep(2)

'# Click on "Över 20 år"'
driver.find_element(By.XPATH, "//*[@id='__next']/div[1]/div[2]/div/section/div/div/div[4]/div/div[2]/a").click()
time.sleep(2)

'# Click on "Accepterar alla kakor"'
driver.find_element(By.XPATH, "//*[@id='modalId']/div[2]/div/button[2]").click()
time.sleep(4)

