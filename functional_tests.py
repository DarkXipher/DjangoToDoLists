from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    
    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # New online app. Visit home page
        self.browser.get('http://localhost:8000')

        #notice that the title of the page mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #Invited to enter a to-do item immediately
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual( inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        #User types to-do item immediately, such as cleaning the dishes
        inputbox.send_keys('Clean the Dishes')

        #when user presses enter, page updates and the page lists
        # "1: Clean the Dishes" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Clean the Dishes')

        #There is still a text box inviting to add additional items
        #enters "Purchase Airline tickets"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Purchase Airline tickets')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)


        #The page updates again, and now shows both items
        self.check_for_row_in_list_table('1: Clean the Dishes')
        self.check_for_row_in_list_table('2: Purchase Airline tickets')

        self.fail("Finish the test!")

        #Site should generate a unique URL, some explanation is needed

        #Revisit the URL and items should still appear on list

if __name__ == '__main__':
    unittest.main(warnings='ignore')