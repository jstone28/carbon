import os
from time import sleep

import unittest 

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(
            '../../repo/android/app/build/apk/app-debug-unaligned.apk'
        )
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_find_elements(self):
        #it's checking the wrong activity


        self.driver.implicitly_wait(30)
        # el = self.driver.find_element_by_accessibility_id('com.voxy.news.view.custom.VoxyButton:id/login')
        el = self.driver.find_element_by_accessibility_id('com.voxy.news.debug:id/login')


        # el = self.driver.find_element(By.id('com.voxy.news.view.custom.VoxyButton:id/login'))
        # self.assertIsNotNone(el)
        # self.driver.back()

        # el = self.driver.find_element_by_name("com.voxy.news.debug:id/login")
        # self.assertIsNotNone(el)

    #     els = self.driver.find_elements_by_android_uiautomator("new UiSelector().clickable(true)")
    #     self.assertEqual(12, len(els))

    #     els = self.driver.find_elements_by_android_uiautomator('new UiSelector().enabled(true)')
    #     self.assertEqual(20, len(els))
    #     self.assertEqual("API Demos", els[7].text)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)