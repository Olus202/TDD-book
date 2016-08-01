from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        # Run the browser
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        # Quite the browser
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_and_retrieve(self):
        # Running the website of the application
        self.browser.get(self.live_server_url)

        # "Lists" in title?
        self.assertIn('Lists', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('list', header_text)

        # Typing the list of things to do.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Type thing to do'
        )

        # Typing "Buy the peacock feathers" in the text box.
        inputbox.send_keys('Buy the peacock feathers')

        # After pressing ENTER, the page has been updated.
        # "1. Buy the peacock feathers" as the element of the list.
        inputbox.send_keys(Keys.ENTER)

        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')


#        table = self.browser.find_element_by_id('id_list_table')
#        rows = table.find_elements_by_tag_name('tr')
#        self.assertIn('1: Buy the peacock feathers', [row.text for row in rows])

        # It's still the text box on the page.
        # Typing "Use the peacock feathers to make a bait" as a second element.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use the peacock feathers to make a bait')
        inputbox.send_keys(Keys.ENTER)

        # The page has been updated again, now it's two elements on the list.

        self.check_for_row_in_list_table('2: Use the peacock feathers to make a bait')
        self.check_for_row_in_list_table('1: Buy the peacock feathers')

        # Now new user Frank wants to use a website.

        ## We will use a new session of the browser to be sure
        ## that any information from Edith list, will not visible in Frank list (e.g. by cookies).
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Frank run the website.
        # He did not find any elements from Edith's list.
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy the peacock feathers', page_text)
        self.assertNotIn('to make a bait', page_text)

        # Frank create a new list by entering a new element.
        # He's list is less interested than Edith's list.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy a milk.')
        inputbox.send_keys(Keys.ENTER)

        # Frank hav also a unique url for he's list.
        frank_list_url = self.browser.current_url
        self.assertRegex(frank_list_url, '/lists/.+')
        self.assertNotEqual(frank_list_url, edith_list_url)

        # It's still any element of Edith's list.
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy the peacock feathers', page_text)
        self.assertIn('Buy a milk.', page_text)

        # Go to the special URL - there it a list of things to do.

        # End.

#unittest.main(warnings='ignore')
