
from selenium.webdriver.common.by import By

class LocatorsSport(object):

    EL1 = (By.XPATH, '//li/a[@title=\'Piłka nożna \']')

    EL2 = (By.XPATH, "//li/a[@title='Kadra ' and ./parent::li[@id='e3_4']]")



