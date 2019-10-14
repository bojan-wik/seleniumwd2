'''
https://learning.oreilly.com/videos/selenium-webdriver-with/9781789131550/9781789131550-video25_3
'''
import unittest

class TestCaseDemo2(unittest.TestCase):

    @classmethod
    # setUpClass is run once for the whole class
    def setUpClass(cls):
        print("*#" * 30)
        print("I will run only once before all tests")
        print("*#" * 30)

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

    @classmethod
    # tearDownClass is run once for the whole class
    def tearDownClass(cls):
        print("*#" * 30)
        print("I will run only once after all tests")
        print("*#" * 30)

if __name__ == "__main__":
    unittest.main(verbosity=2)