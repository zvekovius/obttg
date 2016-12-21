from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

	def test_cannot_add_empty_list_items(self):
		#Edith goes to the home page and accidently tries to submit
		#an empty list item. She hits enter on the empty input box. 
		self.browser.get(self.server_url)
		self.browser.find_element_by_id('id_new_item').send_keys('\n')

		#the home page refreshes, and there is an error saying that 
		#the list items cannot be blank. 
		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text, "You can't have an empty list item")

		#She tries again with test, and it works. 
		self.browser.find_element_by_id('id_new_item').send_keys('Buy Milk\n')
		self.check_for_row_in_list_table('1: Buy milk')

		#She again tries to submit a second blank item.
		self.browser.find_element_by_id('id_new_item').send_keys('\n') 

		#She receives a warning on the list page (not just home).
		self.check_for_row_in_list_table('1: Buy milk')
		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text, "You can't have an empty list item")

		#She can correct it by filling in text. 
		self.browser.find_element_by_id('id_new_item').send_keys('Make tea\n')
		self.check_for_row_in_list_table('1: Buy milk')
		self.check_for_row_in_list_table('2: Make tea')

		self.fail('write me!')
