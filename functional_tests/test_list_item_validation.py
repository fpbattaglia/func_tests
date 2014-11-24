__author__ = 'fpbatta'

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

    def test_cannot_add_empty_list_items(self):
        # user tries to submit an empty list item, hits Enter on empty imput box
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # home page refreshes and there is an error message saying that list item cannot be
        #  blank
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # trying again for some text, and that works
        self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # and a second blank item
        self.get_item_input_box().send_keys('\n')

        #another warning
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # and some text is filled in
        self.get_item_input_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_items(self):
        # starting a new list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies\n')
        self.check_for_row_in_list_table('1: Buy wellies')

        # a duplicate item is inserted
        self.get_item_input_box().send_keys('Buy wellies\n')

        # gets an error message
        self.check_for_row_in_list_table('1: Buy wellies')
        error = self.get_error_element()
        self.assertEqual(error.text, "You've already got this in your list")

    def test_error_messages_are_cleared_on_input(self):
        # starts a new list with an error
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())

        # she starts typing in the box to clear error
        self.get_item_input_box().send_keys('a')
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())
