from Pages.Admin_Login_Page import Login_Page
from Pages.All_Quiz import All_Quiz
from Pages.Create_Batch import Create_Batch
from Utilities.test_Base import test_Base


class Test_Batch_Admin(test_Base):

    def test_login_functionality(self):
        try:
            self.login = Login_Page(self.driver)
            self.login.log.info("Navigating to login page of application HQM...")
            self.login.base_login_to_application()
            self.batch = Create_Batch(self.driver)
            self.batch.navigate_to_Batch_creation_section()
            batch_name = self.batch.create_batch()
            self.allquiz = All_Quiz(self.driver)
            self.allquiz.navigate_to_quiz_section()
            self.allquiz.validate_new_batch(batch_name)
        except Exception as e:
            self.login.log.info("Exception occurred")
            self.login.error(e)
