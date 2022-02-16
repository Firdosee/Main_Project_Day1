from selenium.webdriver.common.by import By
from Config.config import Test_Data
from Pages.Base_Page import Base_Page
from Utilities.test_Base import test_Base

log = test_Base.getLogger()


class All_Quiz(Base_Page):

    All_Quiz_Section = (By.XPATH, "//*[text()='All Quiz']")
    All_quiz_section_total = "//table/tbody/tr"

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_quiz_section(self):
        log.info("Navigating to All Quiz section...")
        self.click_operation(All_Quiz.All_Quiz_Section)
        log.info("Into quiz section")

    def return_total_quiz_number_quizsection(self):
        log.info("Getting total number of quiz present in dashboard")
        rows_num = self.driver.find_elements_by_xpath(All_Quiz.All_quiz_section_total)
        print(type(rows_num))
        log.info(type(rows_num))
        return rows_num
