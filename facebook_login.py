from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "D:/drivers/chromedriver.exe"
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service)

driver.get("https://www.facebook.com/")
time.sleep(2)

email = "first@gmail.com"
password = "fb@123"

driver.find_element(By.ID, "email").send_keys(email)
driver.find_element(By.ID, "pass").send_keys(password)

driver.find_element(By.NAME, "login").click()

time.sleep(15)

driver.quit()


