from selenium import webdriver
import os

class RunChromeTests():

    def test(self):
        driverLocation = "C:/Webdrivers/Chrome/77/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome(driverLocation)
        # Open the provided URL
        driver.get("http://letskodeit.com")


ff = RunChromeTests()
ff.test()