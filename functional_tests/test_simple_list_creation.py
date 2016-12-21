from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class NewVisitorTest(FunctionalTest):
	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get(self.server_url)

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

		inputbox.send_keys('Buy peacock feathers')
		inputbox.send_keys(Keys.ENTER)

		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, '/lists/.+')
		self.check_for_row_in_list_table('1: Buy peacock feathers')	

		inputbox = self.browser.find_element_by_id('id_new_item')
		#user enters 'buy peacock feathers as a todo item.
		inputbox.send_keys('Buy more peacock feathers')

		#user hits enter.
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.check_for_row_in_list_table('1: Buy peacock feathers')	

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.check_for_row_in_list_table('2: Buy more peacock feathers')	

		#New user comes to site.
		self.browser.quit()
		#self.browser = webdriver.Firefox()
		self.browser = browser = webdriver.Firefox(firefox_binary=FirefoxBinary(firefox_path='/home/zvekovius/Downloads/firefox/firefox'))
		
		self.browser.get(self.server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertNotIn('make a fly', page_text)

		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy Milk')
		inputbox.send_keys(Keys.ENTER)

		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/lists/.+')
		self.assertNotEqual(francis_list_url, edith_list_url)

		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertIn('Buy Milk', page_text)
