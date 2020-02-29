# try:
from selenium import webdriver
import time
import unittest
import math

class test_group(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()

    def test_01(self):
        link = "http://suninjuly.github.io/get_attribute.html"
        wd = self.browser
        wd.get(link)
        x = wd.find_element_by_xpath("//img").get_attribute("valuex")
        def calc(x):
            return str(math.log(abs(12 * math.sin(int(x)))))
        y = calc(x)
        input_field = wd.find_element_by_xpath("//input[@id = 'answer']")
        input_field.send_keys(y)
        robo_checkbox = wd.find_element_by_id("robotCheckbox")
        robo_checkbox.click()
        robo_radio = wd.find_element_by_id("robotsRule")
        robo_radio.click()
        submit = wd.find_element_by_xpath("//button")
        submit.click()
        time.sleep(10)



def tearDown(self):
    self.browser.quit()


if __name__ == "__main__":
    unittest.main()

