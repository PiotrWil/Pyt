from time import sleep

import pytest
from selenium import webdriver
from pyassert import *

from Sport import Sport

def input():
    return 'chrome'

@pytest.fixture(params=["chrome"],scope="class")
def fix(request):
    print("BeforeClass")
    if request.param == "chrome":
         option = webdriver.ChromeOptions()
         option.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})
         driver = webdriver.Chrome(options=option, executable_path='C:\\dabag-dev\\chromedriver.exe')
    if request.param == "proba":
        option = webdriver.ChromeOptions()
        option.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})
        driver = webdriver.Chrome(options=option, executable_path='C:\\dabag-dev\\chromedriver.exe')
    request.cls.driver = driver

    yield
    driver.quit()

@pytest.mark.usefixtures("fix")
class Test_nowa_Test():

    # @pytest.fixture
    # def test_aa(self):
    #     print("BeforeTest")
    #     yield self.driver
    #     self.close()


    @pytest.mark.parametrize("a, b", [("https://www.sport.pl/sport-hp/0,0.html", "Sport na Sport.pl - Wyniki i wiadomości sportowe"),
                                      ("https://www.sport.pl/sport-hp/0,0.html", "Sport na Sport.pl - Wyniki i wiadomości sportowe")])
    def test_first(self,a,b):
        self.driver.get(a)
        sport = Sport(self.driver)
        sleep(5)
        assert_that(sport.getName()).is_equal_to(b)

    # def test_first1(self):
    #     self.driver.get("https://www.sport.pl/sport-hp/0,0.html")
    #     sport = Sport(self.driver)
    #     sleep(5)
    #     assert_that(sport.getName()).is_equal_to('Sport na Sport.pl - Wyniki i wiadomości sportowe')