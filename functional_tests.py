from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_list_and_retreive_it_later(self):

        # Edith wants to check out a new to-do app 
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists 
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        # She is invited to enter a to do item right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

        # She type 'buying peacock feathers' in the text box
        inputbox.send_keys('Buy peacock feathers')

        # when she hits enter the page updates with one item 'Buy peacock feathers' as item in a list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows))

        # There is still a text box inviting her to enter another item
        self.fail('Finish the test!')

        # She enters 'Use peacock feathers to make fly'

        # Page updates again an shows both items on the list

        # Edith wonders if the page will remember her lists. 
        # She sees that the page has generated a unique url
        # There is some explanatory text to that effect

        # She visits the url and sees the list is there

        # She is satisfied and goes to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')


