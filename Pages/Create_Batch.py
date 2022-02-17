from selenium.webdriver.common.by import By
from Config.config import Test_Data
from Pages.Base_Page import Base_Page
from Utilities.test_Base import test_Base


class Create_Batch(Base_Page):
    Create_Batch_Section = (By.XPATH, "//*[text()='Batch']")
    Batch_Name = (By.XPATH, "//*[text()='Batch']/following-sibling::input")
    Batch_button = (By.XPATH, "//*[text()='Create']")
    log = test_Base.getLogger()

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_Batch_creation_section(self):
        self.log.info("Navigating to Quiz Creation section...")
        self.click_operation(Create_Batch.Create_Batch_Section)
        self.log.info("Into Quiz creation section")

    def create_batch(self):
        self.log.info("Creating a new batch...")
        t2 = Test_Data()
        batch_text = t2.create_random_text()
        self.send_keys_operation(Create_Batch.Batch_Name, batch_text)
        self.click_operation(Create_Batch.Batch_button)
        return batch_text

