import os
import unittest
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)

class Test2Appium(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Genymotion Cloud'
        desired_caps['app'] = PATH('ApiDemos-debug.apk')
        desired_caps['udid'] = 'localhost:20000'
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'

        desired_caps['noReset'] = 'true'



        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(2)

    def tearDown(self):
        self.driver.quit()

    def testWIFI(self):
        self.driver.is_app_installed('io.appium.android.apis')
        self.driver.find_element_by_accessibility_id('Preference').click()
        self.driver.find_element_by_accessibility_id('3. Preference dependencies').click()

        checkboxes = self.driver.find_elements_by_android_uiautomator('new UiSelector().checkable(true)')

        for el in checkboxes:
            is_checked = self.driver.find_element_by_id('android:id/checkbox').get_attribute('checked')

            if is_checked == 'true':
                print("Wszystkie checkboxy sa zaznaczone")
            else:
                el.click()
                sleep(1)

        passwordInput = '12345'
        self.driver.find_element_by_xpath('//*[@text="WiFi settings"]').click()
        self.driver.find_element_by_class_name('android.widget.EditText').send_keys(passwordInput)

        passwordCurrent = self.driver.find_element_by_class_name('android.widget.EditText').get_attribute('text')

        #asercja
        self.assertEqual(passwordInput,passwordCurrent)
        self.driver.find_element_by_id('android:id/button2').click()

        self.driver.back()
        self.driver.keyevent(4)
        sleep(5)

if __name__ == 'main':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test2Appium)
    unittest.TextTestRunner(verbosity=2).run(suite)