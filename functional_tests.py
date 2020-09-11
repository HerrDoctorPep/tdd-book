from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_list_and_retreive_it_later(self):

        # Edith wants to check out a new to-do app 
        self.browser.get('http://localhost:8000')

        # She notices the page title mentions to-do lists 
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to do item right away

        # She type 'buying peacock feathers' in the text box

        # when she hits enter the page updates with one item 'Buy peacock feathers' as item in a list

        # There is still a text box inviting her to enter another item

        # She enters 'Use peacock feathers to make fly'

        # Page updates again an shows both items on the list

        # Edith wonders if the page will remember her lists. 
        # She sees that the page has generated a unique url
        # There is some explanatory text to that effect

        # She visits the url and sees the list is there

        # She is satisfied and goes to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')


