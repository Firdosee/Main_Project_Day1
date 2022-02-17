import time

from selenium.webdriver.common.by import By
from Config.config import Test_Data
from Pages.Base_Page import Base_Page
from Utilities.test_Base import test_Base


# log = test_Base.getLogger()


class All_Quiz(Base_Page):
    All_Quiz_Section = (By.XPATH, "//*[text()='All Quiz']")
    All_quiz_section_total = "//table/tbody/tr"
    batch_scroll = "(//*[text()='Publish Quiz'])[1]"
    batch_dropdown = "//select[@name='batch']"
    Add_question_description = (By.XPATH, "//*[text()='Question']/following-sibling::textarea")
    option1 = (By.XPATH, "//*[text()='Option 1']/following-sibling::input")
    option2 = (By.XPATH, "//*[text()='Option 2']/following-sibling::input")
    option3 = (By.XPATH, "//*[text()='Option 3']/following-sibling::input")
    option4 = (By.XPATH, "//*[text()='Option 4']/following-sibling::input")
    answer = "//*[text()='Select Answer']/following-sibling::select"
    Marks = (By.XPATH, "//*[text()='Marks']/following-sibling::input")
    Add_question_button = (By.XPATH, "//button[text()=' Add ']")

    log = test_Base.getLogger()

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_quiz_section(self):
        self.log.info("Navigating to All Quiz section...")
        self.click_operation(All_Quiz.All_Quiz_Section)
        self.log.info("Into quiz section")

    def return_total_quiz_number_quizsection(self):
        self.log.info("Getting total number of quiz present in dashboard")
        rows_num = self.driver.find_elements_by_xpath(All_Quiz.All_quiz_section_total)
        print(type(rows_num))
        self.log.info(type(rows_num))
        return rows_num

    def validate_new_batch(self, batch):
        try:
            self.log.info("Validating new batch creation...")
            element = self.driver.find_element_by_xpath(All_Quiz.batch_scroll)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            options = self.get_all_dropdown_option(All_Quiz.batch_dropdown)
            self.log.info("All available options are..." + options)
            if options.find(batch) == -1:
                print("NO")
                a = False
            else:
                print("YES")
                a = True
            assert True == a
            self.log.info("Added Batch is successfully reflected under All quiz section")

        except Exception as e:
            self.log.info("Exception occurred")
            self.log.error(e)

    def Adding_question_to_quiz(self, quiz_name):

        t4 = Test_Data()
        dict_details = t4.getTestData("admin", "AddQuestion")
        publish_quiz = (By.XPATH, "//*[text()='" + quiz_name + "']/parent::tr//button[text()='Publish Quiz']")
        Add_question = "//*[text()='" + quiz_name + "']/parent::tr//button[text()='Add Question']"
        Add_batch = "//*[text()='" + quiz_name + "']/parent::tr/td[5]//select[@name='batch']"
        self.log.info("Adding new questions to quiz...")
        # self.log.info("quiz name is" + quiz)
        element = self.driver.find_element_by_xpath(All_Quiz.batch_scroll)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.log.info(Add_question)
        element = self.driver.find_element_by_xpath(Add_question)
        self.driver.execute_script("arguments[0].click();", element)
        self.send_keys_operation(All_Quiz.Add_question_description, dict_details["question"])
        self.send_keys_operation(All_Quiz.option1, dict_details["option1"])
        self.send_keys_operation(All_Quiz.option2, dict_details["option2"])
        self.send_keys_operation(All_Quiz.option3, dict_details["option3"])
        self.send_keys_operation(All_Quiz.option4, dict_details["option4"])
        self.select_option_byvisibletext(All_Quiz.answer, dict_details["answer"])
        self.send_keys_operation(All_Quiz.Marks, dict_details["marks"])
        self.click_operation(All_Quiz.Add_question_button)
        self.select_option_dropdown(Add_batch, 3)
        select_box = self.driver.find_element_by_xpath(Add_batch)
        options = [x for x in select_box.find_elements_by_tag_name("option")]
        count = 1
        for element in options:
            if count == 4:
                batch = element.text
                self.log.info(batch)
                print(element.text)
                break
            # get_attribute("value"))
            count = count + 1
            time.sleep(5)
        self.click_operation(publish_quiz)
        self.log.info("Quiz is published successfully")
        return batch
