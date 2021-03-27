import os
import unittest
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)

class Test1Appium(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Genymotion Cloud'
        desired_caps['app'] = PATH('ContactManager.apk')
        desired_caps['udid'] = 'localhost:10000'
        desired_caps['appPackage'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = 'com.example.android.contactmanager.ContactManager'


        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(2)

    def tearDown(self):
        self.driver.quit()

    def testForm(self):
        self.driver.is_app_installed('com.example.android.contactmanager')
        self.driver.find_element_by_class_name('android.widget.Button').click()
        textfields = self.driver.find_elements_by_class_name('android.widget.EditText')
        textfields[0].send_keys('Jacek z Przypadkowa')
        textfields[1].send_keys('333222111')
        textfields[2].send_keys('jacek1@cdv.pl')

        sleep(1)

        print(textfields[0])
        print(textfields[0].text)


        self.assertEqual(textfields[0].text, "Jacek z Przypadkowa")
        self.assertEqual(textfields[1].text, "333222111")
        self.assertEqual(textfields[2].text, "jacek1@cdv.pl")

        sleep(1)




        self.assertEqual(textfields[0].text, "Jacek z Przypadkowa")
        self.assertEqual(textfields[1].text, "333222111")
        self.assertEqual(textfields[2].text, "jacek1@cdv.pl")
        self.driver.find_element_by_id('com.example.android.contactmanager:id/contactSaveButton').click()
        errorText = self.driver.find_element_by_id('android:id/alertTitle').text
        self.assertTrue('Contact Manager has stopped' in errorText)
        sleep(3)



if __name__ == 'main':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test1Appium)
    unittest.TextTestRunner(verbosity=2).run(suite)