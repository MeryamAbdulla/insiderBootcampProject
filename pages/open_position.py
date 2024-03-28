from base.base_page import BasePage
from selenium.webdriver.common.by import By

import time

from pages.form_file import FormFile

class OpenPositionPage(BasePage):
    filter_by_location = (By.ID, "select2-filter-by-location-container")
    filter_by_department = (By.ID, "select2-filter-by-department-container")
    job_list = (By.ID, "jobs-list")
    position_class = (By.CLASS_NAME, "position-title")
    view_role = (By.XPATH, "//a[contains(text(), 'View Role')]")

    def __init__(self, driver):
        super().__init__(driver)

    def take_screenshot(self, test_satus):
        filename =f"screenshot_{test_satus}.png"
        self.driver.save_screenshot(filename)

    def click_filter_by_location(self):
        location = self.driver.find_element(*self.filter_by_location)
        location.click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//li[contains(text(), 'Istanbul, Turkey')]").click()

    def click_filter_by_department(self):
        department_container = self.driver.find_element(*self.filter_by_department)
        department_container.click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//li[contains(text(), 'Quality Assurance')]").click()

    def get_job_list(self):
        job_lists = self.driver.find_element(*self.job_list)
        print(job_lists.get_property("textContent"))

    def click_view_role(self):
        view_role_btn = self.driver.find_element(*self.view_role)
        self.driver.execute_script("arguments[0].click();", view_role_btn)
        try:
            test_satus = "passed"
            return FormFile(self.driver)
        except AssertionError:
            test_satus = "failed"
            raise
        finally:
            self.take_screenshot("form " + test_satus)


