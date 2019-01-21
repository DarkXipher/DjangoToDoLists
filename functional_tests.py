from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # New online app. Visit home page
        self.browser.get('http://localhost:8000')

        #notice that the title of the page mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail("Finish the test!")

        #Invited to enter a to-do item immediately

        #User types to-do item immediately, such as cleaning the dishes

        #when user presses enter, page updates and the page lists
        # "1: Clean the Dishes" as an item in a to-do list

        #There is still a text box inviting to add additional items
        #enters "Purchase Airline tickets"

        #The page updates again, and now shows both items

        #Site should generate a unique URL, some explanation is needed

        #Revisit the URL and items should still appear on list

if __name__ == '__main__':
    unittest.main(warnings='ignore')