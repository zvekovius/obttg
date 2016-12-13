from selenium import webdriver
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

		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')
#user enters to-do item. 

#user types "Buy peacock feathers"

#user hits enter and "1: Buy peackcock feather" is the first item in to do list.

#Still another text box to enter new items. 

#User enters "Use Peacock feathers to make a fly"

#The page updates again after hitting enter. 

#User looks to URL for unique identifier to save the list. 

#User goes to that URL, the to-do list is still there (2 items). 

#User quits. 

if __name__ == '__main__':
	unittest.main(warnings='ignore')


