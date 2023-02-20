from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

driver.maximize_window()

#login

driver.find_element(By.ID, "user-name").send_keys("standard_user")

driver.find_element(By.ID, "password").send_keys("secret_sauce")

driver.find_element(By.ID, "login-button").click()


#addremove woman

driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()

driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()

#remover primer item
#driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-backpack\"]").click()


                                       
time.sleep(2)

driver.find_element(By.LINK_TEXT, "2").click()
driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]").click()
driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").send_keys("test")
driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").send_keys("apellido")
driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").send_keys("1090")

time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
  
driver.find_element(By.CSS_SELECTOR, "*[data-test=\"finish\"]").click()
time.sleep(2)

########    LOG OUT #####################
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(1)

driver.find_element(By.ID, "logout_sidebar_link").click()
time.sleep(2)




#driver. quit()

