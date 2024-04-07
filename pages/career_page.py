from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

import time

from pages.quality_assurance import QualityAssurance


class CareerPage(BasePage):
    location = (By.XPATH, '//*[@id="career-our-location"]')
    life_at_insider = (By.CLASS_NAME, "elementor-heading-title")
    find_your_calling_by_id = (By.ID, "career-find-our-calling")
    loadmore_class = (By.CLASS_NAME, "loadmore")
    loadmoredata_class = (By.CLASS_NAME, 'career-load-more')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_page_load()

    def take_screenshot(self, test_satus):
        filename =f"screenshot_{test_satus}.png"
        self.driver.save_screenshot(filename)

    def wait_page_load(self):
        self.wait.until(ec.visibility_of_element_located(self.location))
        self.wait.until(ec.visibility_of_element_located(self.life_at_insider))
        self.wait.until(ec.visibility_of_element_located(self.find_your_calling_by_id))

    def wait_page_load(self):
        self.wait.until(ec.visibility_of_element_located(self.loadmoredata_class))

    def get_life_at_insider(self):
        return self.driver.find_elements(*self.life_at_insider)
    def get_location(self):
        return self.driver.find_element(*self.location)
    def find_your_calling(self):
        return self.driver.find_element(*self.find_your_calling_by_id)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_see_all_teams(self):
        try:
            calling = self.find_your_calling()
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            loadmore_button = calling.find_element(*self.loadmore_class)
            self.scroll_to_element(loadmore_button)
            self.driver.execute_script("arguments[0].click();", loadmore_button)
            test_satus = "passed"
        except AssertionError:
            test_satus = "failed"
            raise
        finally:
            self.take_screenshot("click_see_all_teams " + test_satus)

        self.driver.execute_script("window.scrollTo(1, 1);")

    def click_quality_assurance(self):
        try:
            time.sleep(5)
            loadmoredata = self.driver.find_element(*self.loadmoredata_class)
            elements = loadmoredata.find_elements(By.XPATH,
                                                  '//*[@id="career-find-our-calling"]/div/div/div[2]/div[12]/div[2]/a')
            self.driver.execute_script("arguments[0].click();", elements[0])
            test_status = "passed"
        except AssertionError:
            test_status = "failed"
            raise
        finally:
            self.take_screenshot("quality_assurance_clicked " + test_status)
            return QualityAssurance(self.driver)
