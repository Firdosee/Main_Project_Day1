from Pages.All_Quiz import All_Quiz
from Pages.Login_Page import Login_Page
from Utilities.test_Base import test_Base

logg = test_Base.getLogger()


class Test_Loginn(test_Base):

    def test_login_functionality(self):
        try:
            # global logg
            logg.info("Navigating to login page of application HQM...")
            self.login = Login_Page(self.driver)
            self.login.base_login_to_application()
            logg.info("Login functionality for admin user is successfully validated")
        except Exception as e:
            logg.error("Login functionality for admin user failed")
            logg.info(e)
            assert False

    def test_dashboard_functionality(self):
        try:
            # global logg
            logg.info("Navigating to login page of application HQM...")
            self.login = Login_Page(self.driver)
            self.login.base_login_to_application()
            quiz_list = self.login.return_list_of_all_quiz_row()
            quiz_list = len(quiz_list)
            logg.info(quiz_list)
            total_quiz = self.login.return_total_quiz_number()
            logg.info(total_quiz)
            assert str(quiz_list) == str(total_quiz)
        except Exception as e:
            logg.error("Quiz Count does not match in dashboard")
            logg.info(e)
            assert False
        try:
            self.login.validate_all_dashboard_links()
            logg.info("All links on dashboard are successfully validated")
        except Exception as e:
            logg.error(e)
            logg.info("All links on dashboard are not available")

    def test_Validate_All_Quiz_Section(self):
        try:
            # global logg
            logg.info("Navigating to All Quiz section...")
            self.login = Login_Page(self.driver)
            self.login.base_login_to_application()
            self.all_quiz = All_Quiz(self.driver)
            self.all_quiz.navigate_to_quiz_section()
            quiz_list = self.all_quiz.return_total_quiz_number_quizsection()
            quiz_list = len(quiz_list)
            logg.info(quiz_list)
            self.login.navigate_to_dashboard()
            total_quiz = self.login.return_total_quiz_number()
            logg.info(total_quiz)
            assert str(quiz_list) == str(total_quiz)
            logg.error("Quiz Count is successfully validated in All Quiz section")
        except Exception as e:
            logg.error("Quiz Count does not match in Quiz section")
            logg.info(e)
            assert False


