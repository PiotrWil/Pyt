from time import sleep

import pytest
from selenium import webdriver


@pytest.fixture(params=["a", "b"])
def fix():
    print("ww")
    option = webdriver.ChromeOptions()
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})
    #global driver
    driver = webdriver.Chrome(options=option, executable_path='C:\\dabag-dev\\chromedriver.exe')
    yield driver
    driver.quit()

# with global we can run write driver.get(...) and there is yield without driver
def test_assertsum(fix):
    fix.get("https://www.sport.pl/sport-hp/0,0.html")
    fix.maximize_window()
    sleep(2)
    print("ee")
    # x=fix
    # y=6
    # assert x+y == 6

# def test_1assertsum(fix):
#     fix.get("https://www.sport.pl/sport-hp/0,0.html")
#     fix.maximize_window()
#     sleep(2)
#     x=2
#     y=6
#     assert x+y == 8