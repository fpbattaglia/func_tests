__author__ = 'fpbatta'

from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # user tries to submit an empty list item, hits Enter on empty imput box

        # home page refreshes and there is an error message saying that list item cannot be
        #  blank


        # trying again for some text, and that works

        # and a second blank item

        #another warning

        # and some text is filled in


        self.fail('Write me!')