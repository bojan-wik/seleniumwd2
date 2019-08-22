import os
import time
from selenium import webdriver

class hiddenElements():

    def testLestKodeIt(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice/"
        driverLocation = "C:/SeleniumDriver/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)

        # Find the state of the text box.
        textboxElement = driver.find_element_by_id("displayed-text")
        textboxState = textboxElement.is_displayed()
        print("Text is visible? -> {}.".format(textboxState))
        time.sleep(2)

        # Click the hide button.
        driver.find_element_by_id("hide-textbox").click()
        # Find the state of the text box.
        textboxState = textboxElement.is_displayed()
        print("Text is visible? -> {}.".format(textboxState))
        time.sleep(2)

        # Click the show button.
        driver.find_element_by_id("show-textbox").click()
        # Find the state of the text box.
        textboxState = textboxElement.is_displayed()
        print("Text is visible? -> {}.".format(textboxState))
        time.sleep(2)

        # Browser close.
        driver.quit()


chrome = hiddenElements()
chrome.testLestKodeIt()
