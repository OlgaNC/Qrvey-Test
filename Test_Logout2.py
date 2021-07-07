from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time 

USERNAME= ("standard_user")
PASSWORD=("secret_sauce")

driver = webdriver.Chrome("C:\\Test_Ejemplo\\chromedriver.exe")
driver.get('https://www.saucedemo.com/')

username_textbox = driver.find_element_by_id("user-name")
username_textbox.send_keys(USERNAME)

password_textbox = driver.find_element_by_id("password")
password_textbox.send_keys(PASSWORD)

login_button = driver.find_element_by_name("login-button")
login_button.submit()

print("logged in successfully")

driver.find_element_by_id("add-to-cart-sauce-labs-backpack").click()
time.sleep(2)
driver.find_element_by_id("add-to-cart-sauce-labs-bike-light").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='shopping_cart_container']/a/span").click()
time.sleep(2)
driver.find_element_by_id("remove-sauce-labs-backpack").click()
time.sleep(2)
driver.find_element_by_id("checkout").click()
driver.find_element_by_id("first-name").click()
driver.find_element_by_id("first-name").clear()
time.sleep(2)
driver.find_element_by_id("first-name").send_keys("Olga")
driver.find_element_by_id("last-name").clear()
time.sleep(2)
driver.find_element_by_id("last-name").send_keys("Canabal")
driver.find_element_by_id("postal-code").clear()
time.sleep(2)
driver.find_element_by_id("postal-code").send_keys("760031")
driver.find_element_by_id("continue").click()
time.sleep(2)
driver.find_element_by_id("finish").click()
time.sleep(2)
driver.find_element_by_id("react-burger-menu-btn").click()
time.sleep(2)
driver.find_element_by_id("logout_sidebar_link").click()

driver.quit()





    


