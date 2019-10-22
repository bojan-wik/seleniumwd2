import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class GetText():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice/"
        driverLocation = "C:/Webdrivers/Chrome/77/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        openTabElement = driver.find_element(By.ID, "opentab")
        elementText = openTabElement.text
        print("Text on element is: {}".format(elementText))
        time.sleep(1)
        driver.quit()

chrome = GetText()
chrome.test()