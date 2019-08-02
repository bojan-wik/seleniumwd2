import os
import time
from selenium import webdriver

class RadioButtonsAndCheckboxes():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice/"
        driverLocation = "C:/SeleniumDriver/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        bmwRadioBtn = driver.find_element_by_id("bmwradio")
        bmwRadioBtn.click()
        time.sleep(2)

        benzRadioBtn = driver.find_element_by_id("benzradio")
        benzRadioBtn.click()
        time.sleep(2)

        bmwCheckbox = driver.find_element_by_id("bmwcheck")
        bmwCheckbox.click()
        time.sleep(2)

        benzCheckbox = driver.find_element_by_id("benzcheck")
        benzCheckbox.click()
        time.sleep(2)

        print("Is BMW Radio button selected? {}".format(str(bmwRadioBtn.is_selected())))
        print("Is Benz Radio button selected? {}".format(str(benzRadioBtn.is_selected())))
        print("Is BMW Checkbox selected? {}".format(str(bmwCheckbox.is_selected())))
        print("Is Benz Checkbox button selected? {}".format(str(benzCheckbox.is_selected())))

chrome = RadioButtonsAndCheckboxes()
chrome.test()