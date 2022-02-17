from selenium.webdriver.common.by import By
from Config.config import Test_Data
from Pages.Base_Page import Base_Page
from Utilities.test_Base import test_Base


#log = test_Base().getLogger()


class Login_Page(Base_Page):
    Username = (By.XPATH, "//*[text()='Username']/following-sibling::input")
    PASSWORD = (By.XPATH, "//*[text()='Password']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//*[text()=' Login ']")
    GET_USER_NAME = (By.XPATH, "//*[text()='Admin Admin']")
    Get_Total_rows = "//table/tbody/tr"
    Total_quiz_number = (By.XPATH, "//*[text()='Total Quiz']//following-sibling::span")
    All_links_of_dashboard = "//li//span"
    Dashboard = (By.XPATH, "//*[text()='Dashboard']")
    log = test_Base().getLogger()
    Logout = (By.XPATH, "//*[@class='fa fa-sign-out']")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_dashboard(self):
        self.log.info("Navigating to All Dashboard...")
        self.click_operation(Login_Page.Dashboard)
        self.log.info("Into Dashboard section")

    def logout(self):
        self.log.info("Logging out...")
        self.click_operation(Login_Page.Logout)
        self.log.info("Successfully Logged out")

    def base_login_to_application(self):
        #global log
        dict_d = {}
        self.log.info("Getting Test Data")
        dict_d = Test_Data.getTestData(self, "admin", "login")
        self.log.info(dict_d)
        self.log.info("Entering the url")
        self.enter_url_operation(dict_d["url"], Login_Page.Username)
        self.log.info("Entering the Username")
        self.send_keys_operation(Login_Page.Username, dict_d["username"])
        self.log.info("Entering the Password")
        self.send_keys_operation(Login_Page.PASSWORD, dict_d["password"])
        self.log.info("Clicking login button")
        self.click_operation(Login_Page.LOGIN_BUTTON)
        user = self.get_text_from_locator(Login_Page.GET_USER_NAME)
        self.log.info("Validating if the user is successfully logged in")
        assert user == dict_d["logged_in_user"]
        self.log.info("user is successfully logged in the account")

    def return_list_of_all_quiz_row(self):
        #global log
        self.log.info("Returning the list of all row elements of quiz")
        rows = self.driver.find_elements_by_xpath(Login_Page.Get_Total_rows)
        print(type(rows))
        self.log.info(type(rows))
        return rows

    def return_total_quiz_number(self):
        #global log
        self.log.info("Getting total number of quiz present in dashboard")
        total_quiz = self.get_text_from_locator(Login_Page.Total_quiz_number)
        self.log.info(total_quiz)
        self.log.info(type(total_quiz))
        return total_quiz

    def validate_all_dashboard_links(self):
        # global log
        self.log.info("Getting all links of dashboard")
        links = self.driver.find_elements_by_xpath(Login_Page.All_links_of_dashboard)
        count = len(links)
        count = count + 1
        alllists = ""
        for i in range(1, count, 1):
            j = i
            j = str(j)
            a = self.driver.find_element_by_xpath("(//li//span)[" + j + "]").text
            print(a)
            alllists = alllists + " " + a

        self.log.info("All links in dashboard are" + alllists)
        dict_d = Test_Data.getTestData(self, "admin", "login")
        links_from_excel = dict_d["Dashboard_links"]
        try:
            assert alllists == links_from_excel
            return True
        except Exception as e:
            self.log.error("Exception occurred")
            return False
