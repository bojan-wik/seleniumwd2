import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

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
        time.sleep(2)

        # Search for courses
        searchBox = driver.find_element(By.ID, "search-courses")
        searchBox.send_keys("JavaScript")
        time.sleep(2)
        searchButton = driver.find_element(By.ID, "search-course-button")
        searchButton.click()
        time.sleep(2)

        # Select course
        _course = "//div[contains(@class, 'course-listing-title') and contains(text(), '{0}')]"
        _courseLocator = _course.format("JavaScript for beginners")

        courseElement = driver.find_element(By.XPATH, _courseLocator)
        courseElement.click()
        time.sleep(2)


chrome = DynamicXpathFormat()
chrome.test()