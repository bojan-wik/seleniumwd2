import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class LoginTests:

    def validLogin(self):
        baseUrl = "https://thetestingworld.com/index.php?option=com_users&view=registration&Itemid=588"
        driverLocation = "C:/Tools/Webdrivers/Chrome/79/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)

        nameField = driver.find_element(By.ID, "jform_name")
        nameField.send_keys("Elo rap")

        time.sleep(5)

        act = ActionChains(driver)
        act.send_keys(Keys.TAB).perform()


#chrome = LoginTests()
#chrome.validLogin()

class RunFFTests():

    def testMethod(self):
        # Initiate the driver instance
        driver = webdriver.Firefox(
            executable_path="C:/Tools/Webdrivers/Firefox/geckodriver-v0.26.0-win64/geckodriver.exe")

        driver.get("https://thetestingworld.com/index.php?option=com_users&view=registration&Itemid=588")

        nameField = driver.find_element(By.ID, "jform_name")
        nameField.send_keys("Elo rap")

        time.sleep(2)

        act = ActionChains(driver)
        act.send_keys(Keys.TAB).perform()
        time.sleep(2)
        act.send_keys(Keys.TAB).perform()

ff = RunFFTests()
ff.testMethod()
