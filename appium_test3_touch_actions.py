import os
import unittest
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)

class Test3Appium(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Genymotion Cloud'
        desired_caps['app'] = PATH('ApiDemos-debug.apk')
        desired_caps['udid'] = 'localhost:30000'
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'
        #desired_caps['noReset'] = 'true'


        # connect to Appium
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(2)

    def tearDown(self):
        self.driver.quit()

    def testTouchActions(self):
        self.driver.find_element_by_accessibility_id("Views").click()
        self.driver.find_element_by_accessibility_id("Expandable Lists").click()
        self.driver.find_element_by_accessibility_id("1. Custom Adapter").click()

        peopleNames = self.driver.find_element_by_xpath('//android.widget.TextView[@text = "People Names"]')
        action = TouchAction(self.driver)
        action.long_press(peopleNames).release().perform()
        sleep(3)
        sampleMenu = self.driver.find_element_by_xpath('//android.widget.TextView[@text = "Sample menu"]')
        sleep(2)

        #asercja
        self.assertIsNotNone(sampleMenu)




if __name__ == 'main':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test3Appium)
    unittest.TextTestRunner(verbosity=2).run(suite)