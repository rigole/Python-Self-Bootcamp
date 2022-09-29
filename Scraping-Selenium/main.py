"""
print('\n'.join
 ([''.join
   ([('Engineer'[(x-y)%8 ]
     if((x*0.05)**2+(y*0.1)**2-1)
      **3-(x*0.05)**2*(y*0.1)
       **3<=0 else' ')
        for x in range(-30,30)])
         for y in range(15,-15,-1)]))
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
chrome_driver_path = "C:/chrome/chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"


option = webdriver.ChromeOptions()
#option.add_experimental_option("excludeSwitches", ['enable-logging'])
option.binary_location = brave_path
driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=option)


#time.sleep(10)

driver.get("https://www.pagesjaunes.fr/annuaire/paris-75/developpement-informatique")

time.sleep(55)
#price = driver.find_element_by_id("certified-refurbished-version")
#price = driver.find_element(By.ID, "certified-refurbished-version")
#name = driver.find_element(By.TAG_NAME, "h2")
#class_name = driver.find_element(By.CLASS_NAME, "search-field")

#print(name.tag_name)
#print(name.get_attribute("placeholder"))
#print(class_name)

#frame = driver.find_element(By.NAME, "__tcfapiLocator" )
#driver.switch_to.frame(frame)

name_businness = driver.find_element(By.TAG_NAME, "h1")

#document_link = driver.find_element(By.CSS_SELECTOR, "div.small-widget")
time.sleep(2)
print(name_businness)




#driver.close()
driver.quit()

