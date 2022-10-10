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
 

#assertion cuandp es diferente no muestra assetion error.

assert driver.find_element(By.CSS_SELECTOR, "h2:nth-child(2)").text != "Product successfully added to your shopping cart"

#seguir comprando
#driver.find_element(By.CSS_SELECTOR, ".continue > span").click()

#avanzar en el checkout
driver.find_element(By.CSS_SELECTOR, ".button-medium > span").click()
driver.find_element(By.CSS_SELECTOR, ".standard-checkout > span").click()


#UPDATE DIRECCTION
driver.find_element(By.CSS_SELECTOR, "#address_delivery span").click()
driver.find_element(By.ID, "address2").click()
driver.find_element(By.ID, "address2").send_keys("new direction")
driver.find_element(By.CSS_SELECTOR, "#submitAddress > span").click()
driver.find_element(By.CSS_SELECTOR, ".button:nth-child(4) > span").click()
driver.find_element(By.ID, "cgv").click()
driver.find_element(By.CSS_SELECTOR, ".standard-checkout > span").click()
driver.find_element(By.CSS_SELECTOR, ".bankwire > span").click()
driver.find_element(By.CSS_SELECTOR, "#cart_navigation span").click()


#view history orders
driver.find_element(By.LINK_TEXT, "Back to orders").click()
  
driver.implicitly_wait(3)

#screenshot del order history 
driver.save_screenshot('./history.png')

driver. quit()