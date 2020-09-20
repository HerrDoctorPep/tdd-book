from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10
class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self,row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except(AssertionError,WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])

    def test_can_start_list_and_retreive_it_later(self):

        # Edith wants to check out a new to-do app 
        self.browser.get(self.live_server_url)

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
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text box inviting her to enter another item
        inputbox = self.browser.find_element_by_id('id_new_item')
        
        # She enters 'Use peacock feathers to make fly'
        inputbox.send_keys('Use peacock feathersto makea fly')
        inputbox.send_keys(Keys.ENTER)

       # Page updates again an shows both items on the list

        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathersto makea fly')
        
        # Edith wonders if the page will remember her lists. 
        # She sees that the page has generated a unique url
        # There is some explanatory text to that effect

        # She visits the url and sees the list is there

        # She is satisfied and goes to sleep
        self.fail('Finish the test!')


