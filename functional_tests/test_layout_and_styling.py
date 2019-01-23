from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys

from unittest import skip

class LayoutAndStylingTest(FunctionalTest):
#Skipping this layout test because the chrome driver doesn't seem to handle the text-center correctly
    @skip
    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024,768)

        #She notices the input box is nicely centered
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] / 2, 512, delta=10)

        #she starts a new list and sees the input is nicely centered there too
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] / 2, 512, delta=10)