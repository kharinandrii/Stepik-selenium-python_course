from selenium import webdriver
import time
import unittest
import math





# try:
class test_group(unittest.TestCase):



    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()

    def test_01(self):
        link = "http://suninjuly.github.io/math.html"
        self.browser.get(link)
        x = self.browser.find_element_by_xpath("//span[@id = 'input_value']").text
        def calc(x):
            return str(math.log(abs(12 * math.sin(int(x)))))
        y = calc(x)
        input_field = self.browser.find_element_by_xpath("//input[@id = 'answer']")
        input_field.send_keys(y)
        robot_checkbox = self.browser.find_element_by_xpath("//input[@id = 'robotCheckbox']")
        robot_checkbox.click()
        robot_radiobutton = self.browser.find_element_by_xpath("//input[@id = 'robotsRule']")
        robot_radiobutton.click()
        submit = self.browser.find_element_by_xpath("//button")
        submit.click()
        time.sleep(10)


def tearDown(self):
    self.browser.quit()


if __name__ == "__main__":
    unittest.main()

