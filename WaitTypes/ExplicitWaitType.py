from traceback import print_stack
from Utilities.HandyWrappers import HandyWrappers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import *

class ExplicitWaitType():

    def __init__(self, driver):
        self.driver = driver
        self.HandyWrappers = HandyWrappers(driver)

    def waitForElement(self, locator, locatorType="id",
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.HandyWrappers.getByType(locatorType)
            print("Waiting for maximum :: {} :: seconds for element to be clickable"
                  .format(str(timeout)))
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])

            element = wait.until(expected_conditions.element_to_be_clickable((byType, "stopFilter_stops-0")))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
            print_stack()
        return element