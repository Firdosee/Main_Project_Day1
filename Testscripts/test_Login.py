from Pages.All_Quiz import All_Quiz
from Pages.Admin_Login_Page import Login_Page
from Utilities.test_Base import test_Base


class Test_Loginn(test_Base):

    def test_login_functionality(self):
        try:
            # global logg

            self.login = Login_Page(self.driver)
            self.login.log.info("Navigating to login page of application HQM...")
            self.login.base_login_to_application()
            self.login.log.info("Login functionality for admin user is successfully validated")
            self.login.logout()
        except Exception as e:
            self.login.log.error("Login functionality for admin user failed")
            self.login.log.info(e)
            assert False

    def test_dashboard_functionality(self):
        try:
            # global logg

            self.login = Login_Page(self.driver)
            self.login.log.info("Navigating to login page of application HQM...")
            self.login.base_login_to_application()
            quiz_list = self.login.return_list_of_all_quiz_row()
            quiz_list = len(quiz_list)
            self.login.log.info(quiz_list)
            total_quiz = self.login.return_total_quiz_number()
            self.login.log.info(total_quiz)
            assert str(quiz_list) == str(total_quiz)
        except Exception as e:
            self.login.log.error("Quiz Count does not match in dashboard")
            self.login.log.info(e)
            assert False
        try:
            self.login.validate_all_dashboard_links()
            self.login.log.info("All links on dashboard are successfully validated")
        except Exception as e:
            self.login.log.error(e)
            self.login.log.info("All links on dashboard are not available")
