from selenium import webdriver
import time
import unittest
import math
import os

class test_new(unittest.TestCase):
    def setUp(self) :
        self.wd = webdriver.Chrome()
        self.wd.maximize_window()

    def test(self):
        wd = self.wd
        link = "http://suninjuly.github.io/file_input.html"
        wd.get(link)
        first_name = wd.find_element_by_xpath("//input[@name = 'firstname']")
        first_name.send_keys("Ivan")
        last_name = wd.find_element_by_xpath("//input[@name = 'lastname']")
        last_name.send_keys("Petrov")
        mail = wd.find_element_by_xpath("//input[@name = 'email']")
        mail.send_keys("petro@mail.ru")
        submit_file = wd.find_element_by_xpath("//input[@name = 'file']")
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'text.txt')
        submit_file.send_keys(file_path)
        button = wd.find_element_by_xpath("//button")
        button.click()
        time.sleep(20)

def tearDown(self):
    self.wd.quit()

if __name__ == "__main__":
    unittest.main()