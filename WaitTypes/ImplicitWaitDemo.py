from selenium import webdriver
from selenium.webdriver.common.by import By
import os

class ImplicitWaitDemo():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com"
        driverLocation = "C:/Webdrivers/Chrome/77/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)

        driver.find_element(By.LINK_TEXT, "Login").click()
        emailField = driver.find_element(By.ID, "user_email")
        emailField.send_keys("test@email.com")

chrome = ImplicitWaitDemo()
chrome.test()