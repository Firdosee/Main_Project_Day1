from Pages.Admin_Login_Page import Login_Page
from Pages.All_Quiz import All_Quiz
from Pages.Create_Quiz import Create_Quiz
from Utilities.test_Base import test_Base


class Test_Add_New_Quiz(test_Base):

    def test_e2e_new_quiz_functionality(self):
        try:
            self.login = Login_Page(self.driver)
            self.login.log.info("Navigating to login page of application HQM...")
            self.login.base_login_to_application()
            self.login.log.info("Login functionality for admin user is successfully validated")
            self.create_quiz = Create_Quiz(self.driver)
            self.create_quiz.navigate_to_Quiz_creation_section()
            quizname = self.create_quiz.creating_new_quiz()
            self.Allquiz = All_Quiz(self.driver)
            self.Allquiz.navigate_to_quiz_section()
            a = self.login.is_text_present(quizname)
            #assert True == a
            self.Allquiz.Adding_question_to_quiz(quizname)
        except Exception as e:
            self.login.log.error("Could not add questions to quiz...")
            self.login.log.info(e)
            assert False
