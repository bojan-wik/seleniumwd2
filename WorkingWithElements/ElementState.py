import os
import time
from selenium import webdriver

class elementState():

    def isEnabled(self):
        baseUrl = "https://www.google.com/"
        driverLocation = "C:/SeleniumDriver/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        #e1 = driver.find_element_by_xpath("//form[@id='tsf']//div[@class='a4bIc']/input[@role='combobox']")
        e1 = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[1]/div/div[1]/input")
        e1State = e1.is_enabled()
        print("E1 is enabled -> {}".format(str(e1State)))

        e1.send_keys("cycki")
        time.sleep(5)

e = elementState()
e.isEnabled()