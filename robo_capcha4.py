from selenium import webdriver
import time
import unittest
import math

class test_robot_4(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.maximize_window()

    def test_4(self):
        wd = self.wd
        link = "http://suninjuly.github.io/execute_script.html"
        wd.get(link)
        x = self.wd.find_element_by_xpath("//span[@id = 'input_value']").text
        def calc(x):
            return str(math.log(abs(12 * math.sin(int(x)))))
        y = calc(x)
        wd.execute_script("window.scrollBy(0, 100);")
        input_field = wd.find_element_by_xpath("//input[@id = 'answer']")
        input_field.send_keys(y)
        robo_box = wd.find_element_by_xpath("//input[@id='robotCheckbox']")
        robo_box.click()
        robo_radio = wd.find_element_by_xpath("//input[@id='robotsRule']")
        robo_radio.click()
        button = wd.find_element_by_xpath("//button").click()
        time.sleep(20)



def tearDown(self):
    self.wd.quit()

if __name__ == "__main__":
    unittest.main()
