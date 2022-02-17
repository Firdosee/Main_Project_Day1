from Pages.All_Quiz import All_Quiz
from Pages.Admin_Login_Page import Login_Page
from Utilities.test_Base import test_Base


class Test_All_Quiz(test_Base):
    def test_Validate_All_Quiz_Section(self):
        try:
            # global logg

            self.login = Login_Page(self.driver)
            self.login.log.info("Navigating to All Quiz section...")
            self.login.base_login_to_application()
            self.all_quiz = All_Quiz(self.driver)
            self.all_quiz.navigate_to_quiz_section()
            quiz_list = self.all_quiz.return_total_quiz_number_quizsection()
            quiz_list = len(quiz_list)
            self.login.log.info(quiz_list)
            self.login.navigate_to_dashboard()
            total_quiz = self.login.return_total_quiz_number()
            self.login.log.info(total_quiz)
            assert str(quiz_list) == str(total_quiz)
            self.login.log.error("Quiz Count is successfully validated in All Quiz section")
        except Exception as e:
            self.login.log.error("Quiz Count does not match in Quiz section")
            self.login.log.info(e)
            assert False
