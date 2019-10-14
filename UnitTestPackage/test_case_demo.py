'''
https://learning.oreilly.com/videos/selenium-webdriver-with/9781789131550/9781789131550-video25_2
'''
import unittest

class TestCaseDemo(unittest.TestCase):

    # When a setUp() method is defined, the test runner will run that method prior to each test.
    def setUp(self):
        print("I will run once before every test")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

    # If a tearDown() method is defined, the test runner will invoke that method after each test.
    def tearDown(self):
        print("I will run after every test")

if __name__ == "__main__":
    unittest.main(verbosity=2)