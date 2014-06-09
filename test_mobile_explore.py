import os
from time import sleep
import unittest 
from appium import webdriver
import android



def setUpModule():
    android.setUpLogin()

def tearDownModule():
    android.tearDown()


class TestMobileExplore(unittest.TestCase):

	def test_1_explore(self):
		android.driver.implicitly_wait(10)
		self.assertIsNotNone(android.driver.find_element_by_id('com.voxy.news.debug:id/title'))





# main
if __name__ == '__main__':
    unittest.main(verbosity=2)

