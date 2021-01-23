# from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import os

MAX_WAIT = 10
class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

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

    def test_can_start_list_for_one_user(self):
        # Edith wants to check out a new to-do app 
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention to-do lists 
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        # She is invited to enter a to do item right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

        # She type 'Buy peacock feathers' in the text box
        inputbox.send_keys('Buy peacock feathers')

        # when she hits enter the page updates with one item 'Buy peacock feathers' as item in a list
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text box inviting her to enter another item
        inputbox = self.browser.find_element_by_id('id_new_item')
        
        # She enters 'Use peacock feathers to make fly'
        inputbox.send_keys('Use peacock feathersto make a fly')
        inputbox.send_keys(Keys.ENTER)

       # Page updates again an shows both items on the list

        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathersto make a fly')
        
        # She is satisfied and goes to sleep

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edithstarts a new to do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # She sees that the page has generated a unique url
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # A new user, Francis, comes along on the site
        ## We use a new browser session to make sure that no info 
        ## of Edith's is coming through from cookies etc.

        self.browser.quit()
        self.browser= webdriver.Firefox()

        # Francis visits the home page. There is no sign of Edith's list.
        
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text

        self.assertNotIn('Buy peakock feathers',page_text)
        self.assertNotIn('make a fly',page_text)

        # Francis starts a new list by entering a new item

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Francis gets his own unique url

        francis_list_url = self.browser.current_url
        
        self.assertRegex(edith_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url,edith_list_url)

        #Again thereis no trace of Edith's list

        page_text = self.browser.find_element_by_tag_name('body').text

        self.assertNotIn('Buy peakock feathers',page_text)
        self.assertIn('Buy milk',page_text)

        # Satisfied they both go back to sleep

    def test_layout_and_styling(self):
        # Edith goes to the homepage
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024,768)

        # She notices the box is nicely centered

        inputbox = self.browser.find_element_by_id('id_new_item')

        self.assertAlmostEqual(inputbox.location['x']+inputbox.size['width']/2,512,delta = 10)

        # She starts a new list and sees the input is nicely centered there too

        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(inputbox.location['x']+inputbox.size['width']/2,512,delta = 10)

