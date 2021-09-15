import unittest
from selenium import webdriver

from Sport import Sport
from time import sleep
from pyassert import *

class Basetest(unittest.TestCase):
    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})
        self.driver = webdriver.Chrome(options=option, executable_path='C:\\dabag-dev\\chromedriver.exe')
        self.driver.get("https://www.sport.pl/sport-hp/0,0.html")
        self.driver.maximize_window()

class FirstTest(Basetest):

    def test_flow(self):
        sport = Sport(self.driver)
        assert_that(sport.getName()).is_equal_to('Sport na Sport.pl - Wyniki i wiadomości sportowe')
       # self.assertEqual(sport.getName(),'Sport na Sport.pl - Wyniki i wiadomości sportowe')
        sport.moveToSport()
        sport.goToKadra()
        sleep(2)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
