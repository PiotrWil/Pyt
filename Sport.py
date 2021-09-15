from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

import bb
from BasePage import BasePage
from bb import LocatorsSport
from selenium.webdriver.support import expected_conditions as EC

class Sport(BasePage):

    def getName(self):
        return self.driver.title

    def moveToSport(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(*LocatorsSport.EL1)).perform()
        el2 = self.driver.find_element(*LocatorsSport.EL2)
        wait = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(LocatorsSport.EL2))
        state = WebDriverWait(self.driver, 2).until(lambda driver: self.driver.execute_script('return document.readyState') == 'complete')
        print(state)

    def goToKadra(self):
        el1 = self.driver.find_element(*LocatorsSport.EL2)
        el1.click()

