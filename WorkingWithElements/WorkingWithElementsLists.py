import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class WorkingWithElementsLists():

    def testListOfElements(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice/"
        driverLocation = "C:/SeleniumDriver/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        radioButtonsList = driver.find_elements(
            By. XPATH, "//input[contains(@type, 'radio') and contains(@name, 'cars')]")
        size = len(radioButtonsList)
        print("Size of the list: {}.".format(str(size)))

        for radioButton in radioButtonsList:
            isSelected = radioButton.is_selected()
            if not isSelected:
                radioButton.click()
                time.sleep(2)

chrome = WorkingWithElementsLists()
chrome.testListOfElements()