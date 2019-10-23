from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
from WaitTypes.ExplicitWaitType import ExplicitWaitType

class ExplicitWaitDemo():

    def test(self):
        baseUrl = "https://www.expedia.com/"
        driverLocation = "C:/Webdrivers/Chrome/77/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.implicitly_wait(.5)
        wait = ExplicitWaitType(driver)
        driver.maximize_window()
        driver.get(baseUrl)

        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        # time.sleep(2)
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("POZ")
        # time.sleep(2)
        driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("WAW")
        # time.sleep(2)
        driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("10/30/2019")
        # time.sleep(2)
        returnDate = driver.find_element(By.ID, "flight-returning-hp-flight")
        returnDate.clear()
        # time.sleep(2)
        returnDate.send_keys("11/10/2019")
        # time.sleep(2)
        driver.find_element(By.XPATH, "/html//form[@id='gcw-flights-form-hp-flight']//button[@type='submit']").click()

        element = wait.waitForElement("stopFilter_stops-0")
        element.click()

        time.sleep(2)
        driver.quit()

chrome = ExplicitWaitDemo()
chrome.test()