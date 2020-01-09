from selenium import webdriver

class RunFFTests():

    def testMethod(self):
        # Initiate the driver instance
        driver = webdriver.Firefox(
            executable_path="C:/Tools/Webdrivers/Firefox/geckodriver-v0.26.0-win64/geckodriver.exe")

        driver.get("http://letskodeit.com")

ff = RunFFTests()
ff.testMethod()