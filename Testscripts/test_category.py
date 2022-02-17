from Pages.All_Quiz import All_Quiz
from Pages.Admin_Login_Page import Login_Page
from Pages.Create_Quiz import Create_Quiz
from Pages.Quiz_Category import Quiz_Category
from Utilities.test_Base import test_Base


class Test_Category(test_Base):

    def test_category_creation_functionality(self):
        try:
            # global logg

            self.login = Login_Page(self.driver)
            self.login.log.info("Navigating to Login section...")
            self.login.base_login_to_application()
            self.quiz_category = Quiz_Category(self.driver)
            self.quiz_category.navigate_to_category_section()
            categoryadded = self.quiz_category.create_category()
            self.create_quiz = Create_Quiz(self.driver)
            self.create_quiz.navigate_to_Quiz_creation_section()
            self.create_quiz.validate_category_present(categoryadded)
        except Exception as e:
            self.login.log.info("Exception occurred")
            self.login.log.error(e)
