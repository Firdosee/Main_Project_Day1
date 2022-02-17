from datetime import time

from selenium.webdriver.common.by import By
from Config.config import Test_Data
from Pages.Base_Page import Base_Page
from Utilities.test_Base import test_Base


# log = test_Base.getLogger()


class Create_Quiz(Base_Page):
    Create_Quiz_Section = (By.XPATH, "//*[text()='Quiz']")
    Category_dropdown_Name = "//select[@ng-reflect-name ='category']"
    Create_quiz_button = (By.XPATH, "//*[text()='Create']")
    log = test_Base.getLogger()
    quiz_title = (By.XPATH, "//*[text()='Quiz Title']/following-sibling::input")
    Select_Category_dropdown = "//select[@ng-reflect-name ='category']"

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_Quiz_creation_section(self):
        self.log.info("Navigating to Quiz Creation section...")
        self.click_operation(Create_Quiz.Create_Quiz_Section)
        self.log.info("Into Quiz creation section")

    def validate_category_present(self, category):
        try:
            self.log.info("Validating if category is present...")
            options = self.get_all_dropdown_option(Create_Quiz.Category_dropdown_Name)
            self.log.info("All available options are..." + options)
            if options.find(category) == -1:
                print("NO")
                a = False
            else:
                print("YES")
                a = True
            assert True == a
            self.log.info("Added category is successfully reflected under Add a new quiz section")
        except Exception as e:
            self.log.info("Exception occurred")
            self.log.error(e)

    def creating_new_quiz(self):
        try:
            self.log.info("Creating a new quiz")
            t3 = Test_Data()
            quiz_name = "Hash" + t3.create_random_text()
            self.send_keys_operation(Create_Quiz.quiz_title, quiz_name)
            self.select_option_dropdown(Create_Quiz.Select_Category_dropdown, 3)
            self.click_operation(Create_Quiz.Create_quiz_button)
            self.log.info("Clicking on create quiz button...")
            return quiz_name
        except Exception as e:
            self.log.info("Exception occurred")
            self.log.error(e)
