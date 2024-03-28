from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from base.base_page import BasePage
from pages.career_page import CareerPage

import time


class HomePage(BasePage):
    company_link = (By.XPATH, "//a[contains(text(), 'Company')]")
    dropdown_careers_link = (By.XPATH, "//a[contains(text(), 'Careers')]")

    def __init__(self, driver):
        super().__init__(driver)

    def take_screenshot(self, test_satus):
        filename =f"screenshot_{test_satus}.png"
        self.driver.save_screenshot(filename)

    def click_company_link(self):
        try:
            self.driver.find_element(*self.company_link).click()
            test_satus = "passed"
        except AssertionError:
            test_satus = "failed"
            raise
        finally:
            self.take_screenshot("company_link_clicked " + test_satus)
        time.sleep(2)

    def click_career_link(self):
        self.driver.find_element(*self.dropdown_careers_link).click()
        return CareerPage(self.driver)
        time.sleep(2)

