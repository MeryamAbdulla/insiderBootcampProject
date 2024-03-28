import time
from base.base_page import BasePage
from selenium.webdriver.common.by import By

from pages.open_position import OpenPositionPage
class QualityAssurance(BasePage):

    see_all_jobs_button = (By.XPATH, "//a[contains(text(), 'See all QA jobs')]")

    def __init__(self, driver):
        super().__init__(driver)


    def take_screenshot(self, test_satus):
        filename =f"screenshot_{test_satus}.png"
        self.driver.save_screenshot(filename)

    def see_all_jobs(self):
        self.driver.find_element(*self.see_all_jobs_button).click()
        return OpenPositionPage(self.driver)
        time.sleep(3)
