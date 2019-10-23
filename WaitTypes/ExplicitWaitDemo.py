from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

class ExplicitWaitDemo():

    def test(self):
        baseUrl = "https://www.expedia.com/"
        driverLocation = "C:/Webdrivers/Chrome/77/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.get(baseUrl)

        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        time.sleep(2)
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("POZ")
        time.sleep(2)
        driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("WAW")
        time.sleep(2)
        driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("10/30/2019")
        time.sleep(2)
        returnDate = driver.find_element(By.ID, "flight-returning-hp-flight")
        returnDate.clear()
        time.sleep(2)
        returnDate.send_keys("11/10/2019")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='gcw-flights-form-hp-flight']/div[7]/label/button")

chrome = ExplicitWaitDemo()
chrome.test()