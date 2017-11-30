# coding: utf-8
import unittest

import time
from selenium import webdriver


class FindElementTest(unittest.TestCase):

    def setUp(self):
        desired_capabilities = {'aut': 'io.selendroid.testapp'}

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities
        )
        self.driver.implicitly_wait(30)

    def test_find_element_by_id(self):
        time.sleep(5)
        print('111111111111111111111111111')
        self.driver.get('and-activity://io.selendroid.testapp.HomeScreenActivity')
        time.sleep(5)
        print('222222222222222222222222222')
        self.assertTrue("and-activity://HomeScreenActivity" in self.driver.current_url)
        time.sleep(5)
        print('333333333333333333333333333')
        my_text_field = self.driver.find_element_by_id('my_text_field')
        time.sleep(5)
        print('444444444444444444444444444')
        my_text_field.send_keys('hello selendroid')
        time.sleep(5)
        print('555555555555555555555555555')
        self.assertTrue('hello selendroid' in my_text_field.text)
        time.sleep(5)
        print('666666666666666666666666666')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
