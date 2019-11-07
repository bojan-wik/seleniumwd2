'''
https://learning.oreilly.com/videos/selenium-webdriver-with/9781789131550/9781789131550-video25_6
'''
import unittest
from UnittestPackage.test_case_demo1 import TestCaseDemo1
from UnittestPackage.test_case_demo2 import TestCaseDemo2

# Get all tests from TestCaseDemo1 and TestCaseDemo2
tcd1 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo1)
tcd2 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo2)

# Create a test suite combining TestCaseDemo1 and TestCaseDemo2
smoke_test = unittest.TestSuite([tcd1, tcd2])

# Run the test suite
unittest.TextTestRunner(verbosity=1).run(smoke_test)