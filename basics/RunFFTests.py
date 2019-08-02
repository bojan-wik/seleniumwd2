from selenium import webdriver

class RunFFTests():

    def testMethod(self):
        # Initiate the driver instance
        driver = webdriver.Firefox(executable_path="geckodriver-location")

        driver.get("http://letskodeit.com")

ff = RunFFTests()
ff.testMethod()