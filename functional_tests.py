from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        # Run the browser
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        # Quite the browser
        self.browser.quit()

    def test_can_start_and_retrieve(self):
        # Running the website of the application
        self.browser.get('http://localhost:8000')

        # "Lists" in title?
        self.assertIn('Lists', self.browser.title)
        self.fali('End of test!')

        # Typing the list of things to do.

        # Typing "Buy the peacock feathers" in the text box.

        # After pressing ENTER, the page has been updated.
        # "1. Buy the peacock feathers" as the element of the list.

        # It's still the text box on the page.
        # Typing "Use the peacock feathers to make a bait" as a second element.

        # The page has been updated again, now it's two elements on the list.

        # Is it remember on the site? It generated special url with the comment.

        # Go to the special url - there it a list of things to do.

        # End.

if __name__ == '__main__':
    unittest.main(warnings='ignore')