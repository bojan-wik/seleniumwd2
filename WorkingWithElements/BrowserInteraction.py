from selenium import webdriver
import os

class BrowserInteractions():

    def test(self):
        driverLocation = "C:/SeleniumDriver/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        baseUrl = "https://letskodeit.teachable.com/p/practice"

        # Window maximize
        driver.maximize_window()
        # Open the provided URL
        driver.get(baseUrl)
        # Get title
        webPageTitle = driver.title
        print("Title of the web page is: {}".format(webPageTitle))
        # Get current URL
        currentUrl = driver.current_url
        print("Current URL of the web page is: {}".format(currentUrl))
        # Browser refresh
        driver.refresh()
        print("Browser refreshed 1st time")
        driver.get(driver.current_url)
        print("Browser refreshed 2nd time")
        # Open another Url
        driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")
        currentUrl = driver.current_url
        print("Current URL of the web page is: {}".format(currentUrl))
        # Browse back
        driver.back()
        print("Go one step back in browser history")
        currentUrl = driver.current_url
        print("Current URL of the web page is: {}".format(currentUrl))
        # Browser forward
        driver.forward()
        print("Go one step forward in browser history")
        currentUrl = driver.current_url
        print("Current URL of the web page is: {}".format(currentUrl))
        # Get page source
        webPageSource = driver.page_source
        # Browser close / quit
        # driver.close()
        driver.quit()

chrome = BrowserInteractions()
chrome.test()