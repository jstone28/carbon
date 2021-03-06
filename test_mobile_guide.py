import os
from time import sleep
import unittest 
from appium import webdriver
import android



def setUpModule():
    android.setUpLogin()

def tearDownModule():
    android.tearDown()


class TestMobileGuide(unittest.TestCase):

	def test_1_guide_items(self):
		android.driver.implicitly_wait(10)
		self.assertIsNotNone(android.driver.find_element_by_id('com.voxy.news.debug:id/title'))
		self.assertIsNotNone(android.driver.find_element_by_id('com.voxy.news.debug:id/goalsTitle'))
		# swipe right
		android.driver.execute_script("mobile: swipe", {"touchCount": 1 , "startX": 693,
		 "startY": 818, "endX": 224, "endY": 833, "duration": 1.216719 })
		sleep(3)
		# swipe right
		android.driver.execute_script("mobile: swipe", {"touchCount": 1 ,
		 "startX": 718, "startY": 778, "endX": 239, "endY": 781, "duration": 1.201836 })
		sleep(3)
		# swipe left
		android.driver.execute_script("mobile: swipe", {"touchCount": 1 ,
		 "startX": 118, "startY": 820, "endX": 531, "endY": 824, "duration": 1.307949 })
		sleep(3)
		#verify text
		self.assertIsNotNone(android.driver.find_element_by_id('com.voxy.news.debug:id/snapshot'))
		self.assertIsNotNone(android.driver.find_element_by_id('com.voxy.news.debug:id/currentLevel'))

		android.driver.find_element_by_id('com.voxy.news.debug:id/skipResourceButton').click()
		sleep(1)
		android.driver.find_element_by_id('com.voxy.news.debug:id/skipResourceButton').click()
		sleep(1)
		android.driver.find_element_by_id('com.voxy.news.debug:id/flipToPlanner').click()
		sleep(1)
		self.assertIsNotNone(android.driver.find_element_by_id('com.voxy.news.debug:id/goalsTitle'))
		sleep(1)
		android.driver.find_element_by_id('com.voxy.news.debug:id/flipToResource').click()
		sleep(2)
		# click side drawer
		android.driver.find_element_by_id('com.voxy.news.debug:id/currentLevel').click()
		sleep(1)
		android.driver.find_element_by_name('Navigate up').click()
		sleep(2)








# main
if __name__ == '__main__':
    unittest.main(verbosity=2)