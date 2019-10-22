import os
from selenium import webdriver
from selenium.webdriver.common.by import By

class DynamicXpathFormat():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com"
        driverLocation = "C:/Webdrivers/Chrome/77/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        # Login
        driver.find_element(By.LINK_TEXT, "Login").click()
        email = driver.find_element(By.ID, "user_email")
        email.send_keys("test@email.com")
        password = driver.find_element(By.ID, "user_password")
        password.send_keys("abcabc")
        driver.find_element(By.NAME, "commit").click()

        # Search for courses
        searchBox = driver.find_element(By.ID, "search-courses")
        searchBox.send_keys("JavaScript")




chrome = DynamicXpathFormat()
chrome.test()