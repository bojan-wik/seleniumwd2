import os
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

class dropdownSelect():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice/"
        driverLocation = "C:/SeleniumDriver/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        dropdownList = driver.find_element_by_id("carselect")
        sel = Select(dropdownList)

        sel.select_by_value("benz")
        print("Select Benz by value")
        time.sleep(2)

        sel.select_by_index(2)
        print("Select Honda by index")
        time.sleep(2)

        sel.select_by_visible_text("BMW")
        print("Select BMW by visible text")

chrome = dropdownSelect()
chrome.test()