# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver

class FindElementTest(unittest.TestCase):

    def setUp(self):

        '''
        SelendroidConfiguration config = new SelendroidConfiguration();
// Add the selendroid-test-app to the standalone server
config.addSupportedApp("src/main/resources/selendroid-test-app-0.17.0.apk");
selendroidServer = new SelendroidLauncher(config);
selendroidServer.launchSelendroid();
        :return:
        '''


        desired_capabilities = {'aut': 'com.ushaqi.zhuishushenqi'}

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
