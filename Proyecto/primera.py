from lib2to3.pgen2.token import EQUAL
from multiprocessing.connection import wait
from xml.dom.minidom import Element
from xml.etree.ElementTree import ElementTree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()

driver.get("http://automationpractice.com/index.php")

driver.maximize_window()

#login
driver.find_element(By.LINK_TEXT, "Sign in").click()

driver.find_element(By.ID, "email").send_keys("jtegui@gmail.com")

driver.find_element(By.ID, "passwd").send_keys("Abcd1234")

driver.find_element(By.CSS_SELECTOR, "#SubmitLogin > span").click()


#compras woman

driver.find_element(By.CSS_SELECTOR, ".sf-with-ul[title='Women']").click()

driver.execute_script("window.scrollTo(0, 900)") 

hoverable = driver.find_element(By.CSS_SELECTOR, ".product_list > li:nth-of-type(1)")
ActionChains(driver)\
        .move_to_element(hoverable)\
        .perform()

driver.find_element(By.CSS_SELECTOR, ".button[data-id-product='1'] > span").click()

driver.implicitly_wait(8)
 
#driver.find_element(By.CSS_SELECTOR, "#header > div:nth-child(3)").click()

#assertion

assert driver.find_element(By.CSS_SELECTOR, "h2:nth-child(2)").text != "Product successfully added to your shopping cart"


driver.find_element(By.CSS_SELECTOR, ".continue > span").click()


########################
##driver.find_element(By.CSS_SELECTOR, ".ajax_block_product:nth-child(3) .button:nth-child(1) > span").click()
##driver.find_element(By.CSS_SELECTOR, ".continue > span").click()
  
