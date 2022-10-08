from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("http://automationpractice.com/index.php")

driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Sign in").click()

driver.find_element(By.ID, "email").send_keys("jtegui@gmail.com")

driver.find_element(By.ID, "passwd").send_keys("Abcd1234")

driver.find_element(By.CSS_SELECTOR, "#SubmitLogin > span").click()