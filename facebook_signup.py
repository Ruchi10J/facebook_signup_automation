from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

service = Service("D:/drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.facebook.com/")
time.sleep(2)


driver.find_element(By.LINK_TEXT, "Create new account").click()
time.sleep(3)

driver.find_element(By.NAME, "firstname").send_keys("Ruchi")
driver.find_element(By.NAME, "lastname").send_keys("Jaya")

Select(driver.find_element(By.NAME, "birthday_day")).select_by_value("10")
Select(driver.find_element(By.NAME, "birthday_month")).select_by_value("8")
Select(driver.find_element(By.NAME, "birthday_year")).select_by_value("2000")

driver.find_element(By.XPATH, "//input[@value='2']").click()
driver.find_element(By.NAME, "reg_email__").send_keys("first@gmail.com")
time.sleep(3)
driver.find_element(By.NAME, "reg_passwd__").send_keys("fb@123")
driver.find_element(By.NAME, "websubmit").click()

time.sleep(20)
driver.quit()