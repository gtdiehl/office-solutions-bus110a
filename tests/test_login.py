from app.database import Database
from app.loginfunction import login
from tests.input_test_base import set_keyboard_input, get_display_output
import pytest


@pytest.mark.usefixtures("setup_db")
class TestLogin:
    @pytest.mark.parametrize("test_input_name, test_input_password",
                             [("nora.chang@gmail.com", "nora"),
                              ("elanor.white@gmail.com", "elanor")])
    def test_login_success(self, setup_db, test_input_name, test_input_password):
        test_db = Database(setup_db)
        set_keyboard_input([test_input_name, test_input_password])
        result = login(test_db).login()
        output = get_display_output()
        assert output == ["Please enter email: ", "Please enter password: ", "\nLogin Successful"]
        assert result == True

    @pytest.mark.parametrize("test_input_name_1, test_input_password_1, test_input_name_2, test_input_password_2, "
                             "test_input_name_3, test_input_password_3",
                             [("nora.chang@gmail.com", "no", "nora.chang@gmail.com", "no", "nora.chang@gmail.com",
                               "no")])
    def test_login_failure(self, setup_db, test_input_name_1, test_input_password_1, test_input_name_2,
                           test_input_password_2, test_input_name_3, test_input_password_3):
        test_db = Database(setup_db)
        set_keyboard_input([test_input_name_1, test_input_password_1, test_input_name_2, test_input_password_2,
                            test_input_name_3, test_input_password_3])
        result = login(test_db).login()
        output = get_display_output()
        assert output == ["Please enter email: ", "Please enter password: ",
                          "Unsuccessful login attempt.  Please try again. Note that e-mail addresses and passwords are "
                          "case-sensitive.", "Please enter email: ", "Please enter password: ", "Unsuccessful login "
                          "attempt.  Please try again. Note that e-mail addresses and passwords are case-sensitive.",
                          "Please enter email: ", "Please enter password: ", "Unsuccessful login attempt. Note that "
                          "e-mail addresses and passwords are case-sensitive.", "Please contact your administrator for "
                          "your login credentials."]
        assert result == False