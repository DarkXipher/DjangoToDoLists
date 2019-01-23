from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_for_one_user(self):
        # New online app. Visit home page
        self.browser.get(self.live_server_url)

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
        self.wait_for_row_in_list_table('1: Clean the Dishes')

        #There is still a text box inviting to add additional items
        #enters "Purchase Airline tickets"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Purchase Airline tickets')
        inputbox.send_keys(Keys.ENTER)


        #The page updates again, and now shows both items
        self.wait_for_row_in_list_table('1: Clean the Dishes')
        self.wait_for_row_in_list_table('2: Purchase Airline tickets')
    
    def test_multiple_users_can_start_lists_at_different_urls(self):
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        #should be a unique url for user edith
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        #a new user comes by
        #A new browser session needs to be generated to make sure that no information is being leaked over
        self.browser.quit()
        self.browser = webdriver.Chrome()

        #New user, francis visits the home page. There is no trace of Edith's list.
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        #Francis starts a new list by entering a new item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy Milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy Milk')

        #Again, no trace of edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy Milk', page_text)