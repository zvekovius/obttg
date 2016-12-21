from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

	def test_cannot_add_empty_list_items(self):
		#Edith goes to the home page and accidently tries to submit
		#an empty list item. She hits enter on the empty input box. 


		#the home page refreshes, and there is an error saying that 
		#the list items cannot be blank. 

		#She tries again with test, and it works. 

		#She again tries to submit a second blank item. 

		#She receives a warning on the list page (not just home).

		#She can correct it by filling in text. 

		self.fail('write me!')
