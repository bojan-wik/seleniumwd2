'''
https://learning.oreilly.com/videos/selenium-webdriver-with/9781789131550/9781789131550-video25_4
'''
import unittest

class AssertDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a, "a is not true")
        b = False
        self.assertTrue(b, "b is not true")
        self.assertFalse(b, "b is not false")

    def test_assertEqual(self):
        a = "Tester"
        b = "Test"
        self.assertEqual(a, b, "a is not equal b")

if __name__ == "__main__":
    unittest.main(verbosity=2)