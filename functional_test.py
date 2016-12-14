from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = browser = webdriver.Firefox(firefox_binary=FirefoxBinary(firefox_path='/home/zvekovius/Downloads/firefox/firefox'))
		#Wait for awhile. Not great. /explicit/
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get('http://localhost:8000')

		#User notices page title includes to-do.
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		#user is invited to enter a to-do item.
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		#user enters 'buy peacock feathers as a todo item.
		inputbox.send_keys('Buy peacock feathers')

		#user hits enter.
		input.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1. Buy peacock feathers' for row in rows)
		)

		#User wants to add another to-do item. 
		self.fail('finish the test!')

		#The page updates again, and now shows both items on her list.

if __name__ == '__main__':
	unittest.main(warnings='ignore')


