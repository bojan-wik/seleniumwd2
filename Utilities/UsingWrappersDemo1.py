import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities.HandyWrappers import HandyWrappers

class UsingWrappers():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice/"
        driverLocation = "C:/Webdrivers/Chrome/77/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)

        textField1 = hw.getElement("name", "id")
        textField1.send_keys("Test")
        time.sleep(3)
        textField2 = hw.getElement("//*[@id='name']", "xpath")
        textField2.clear()

chrome = UsingWrappers()
chrome.test()