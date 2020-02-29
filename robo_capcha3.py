from selenium import webdriver
import time
import unittest
import math

from selenium.webdriver.support.select import Select


class test_robo_3(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.maximize_window()

    def test_robo_3(self):
        wd = self.wd
        link = "http://suninjuly.github.io/selects1.html"
        wd.get(link)
        x = wd.find_element_by_id("num1").text
        y = wd.find_element_by_id("num2").text
        res = int(x) + int(y)
        select = Select(wd.find_element_by_id("dropdown"))
        select.select_by_value(str(res))
        button = wd.find_element_by_xpath("//button")
        button.click()
        time.sleep(20)


def tearDown(self):
    self.wd.quit()

if __name__ == "__main__":
    unittest.main()