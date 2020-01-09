from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities.HandyWrappers import HandyWrappers
import os

class ElementPresenceCheck():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice/"
        driverLocation = "C:/Webdrivers/Chrome/77/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)

        elementResult1 = hw.isElementPresent("name", By.ID)
        print(str(elementResult1))

        elementResult2 = hw.elementPresenceCheck("//*[@id='yoooo']", By.XPATH)
        print(str(elementResult2))


chrome = ElementPresenceCheck()
chrome.test()