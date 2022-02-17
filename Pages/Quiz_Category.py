from selenium.webdriver.common.by import By
from Config.config import Test_Data
from Pages.Base_Page import Base_Page
from Utilities.test_Base import test_Base

#log = test_Base.getLogger()


class Quiz_Category(Base_Page):
    Category_Section = (By.XPATH, "//*[text()='Category']")
    Category_Name = (By.XPATH, "//*[@id = 'categoryName']")
    Create_category_button = (By.XPATH, "//*[text()='Create']")
    log = test_Base.getLogger()

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_category_section(self):
        self.log.info("Navigating to Category section...")
        self.click_operation(Quiz_Category.Category_Section)
        self.log.info("Into Category section")

    def create_category(self):
        self.log.info("creating a new category...")
        t = Test_Data()
        category_text = t.create_random_text()
        self.log.info("category name is" + " "+category_text)
        self.send_keys_operation(Quiz_Category.Category_Name, category_text)
        self.click_operation(Quiz_Category.Create_category_button)
        return category_text












