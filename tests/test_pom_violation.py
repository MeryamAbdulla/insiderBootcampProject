import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_test import BaseTest
from pages.home_page import HomePage
from pages.career_page import CareerPage
from pages.quality_assurance import QualityAssurance


class TestPomViolation(BaseTest):

    driver = 'chrome'



    def test_pom_violation(self):
        home_page = HomePage(self.driver)
        home_page.click_company_link()
        career_page = home_page.click_career_link()
        location = career_page.get_location()
        life_insider = career_page.get_life_at_insider()
        find_your_calling = career_page.find_your_calling()
        career_page.click_see_all_teams()

        if isinstance(career_page, CareerPage):
            try:
                self.assertTrue(location.text and life_insider and find_your_calling)
                print("OK")
            except AssertionError as e:
                print("AssertionError occurred:", e)
                raise e

            quality_assurance = career_page.click_quality_assurance()
            time.sleep(5)
            open_position = quality_assurance.see_all_jobs()
            time.sleep(6)
            open_position.click_filter_by_location()
            open_position.click_filter_by_department()
            time.sleep(3)
            open_position.get_job_list()
            open_position.click_view_role()

        time.sleep(3)