from app.database import Database
from app.loginfunction import login
from tests.input_test_base import set_keyboard_input, get_display_output
import pytest

@pytest.mark.usefixtures("setup_db")
class TestLogin:
    def test_login_success(self, setup_db):
        test_db = Database(setup_db)
        set_keyboard_input(["nora.chang@gmail.com", "nora"])
        result = login(test_db).login()
        output = get_display_output()
        assert output == ["Please enter email: ", "Please enter password: ", "Login Successful"]
        assert result == True

    def test_login_failure(self, setup_db):
        test_db = Database(setup_db)
        set_keyboard_input(["nora.chang@gmail.com", "no", "nora.chang@gmail.com", "no", "nora.chang@gmail.com", "no"])
        result = login(test_db).login()
        output = get_display_output()
        assert output == ["Please enter email: ", "Please enter password: ",
                          "Unsuccessful login attempt.  Please try again.", "Please enter email: ",
                          "Please enter password: ", "Unsuccessful login attempt.  Please try again.",
                          "Please enter email: ", "Please enter password: ", "Unsuccessful login attempt.",
                          "Please contact your administrator for your login credentials."]
        assert result == False