from selenium.webdriver.common.by import By
from selenium import webdriver;
import time ;

driver = webdriver.Chrome(executable_path=r"/home/juzcategui/Descargas/chromedriver_linux64/chromedriver");


driver.get("http://selenium.dev");

driver.maximize_window();

##time.sleep(3)

vegetable = driver.find_element(By.XPATH, "//h4[@class='h3 mb-3 selenium-webdriver']").text;



print(vegetable);


driver.quit()