from app.database import Database
from app.Add_User import UserController
import pytest


@pytest.mark.usefixtures("setup_db")
class TestUser:
    def test_add_user_success(self):
        pass

    def test_add_user_failure(self):
        pass

    @pytest.mark.parametrize("test_input,expected",
                             [("greg", True),
                              ("Greg", True),
                              ("greg greg", False),
                              ("a", True),
                              ("098743fdsf", False),
                              ("lkj43525", False),
                              ("fred@@", False)])
    def test_verify_user_name(self, setup_db, test_input, expected):
        mydb = Database(setup_db)
        user = UserController(mydb)
        assert user._verifyUserName(test_input) == expected

    @pytest.mark.parametrize("test_input,expected",
                             [("1", True),
                              ("1234567", True),
                              ("abcdefg", True),
                              ("12345678", True),
                              ("mypassis__", False),
                              ("password@@", False),
                              ("1234567890123", True),
                              ("123456789012", True)])
    def test_verify_password(self, setup_db, test_input, expected):
        mydb = Database(setup_db)
        user = UserController(mydb)
        assert user._verifyPassword(test_input) == expected

    @pytest.mark.parametrize("test_input,expected",
                             [("greg@greg.com", True),
                              ("fred@yahoo.com.br", True),
                              ("tom@f.c", False),
                              ("uri@jo.io", True),
                              ("myp", False),
                              ("@", False),
                              ("passwor@", False)])
    def test_verify_email_address(self, setup_db, test_input, expected):
        mydb = Database(setup_db)
        user = UserController(mydb)
        assert user._verifyEmailAddress(test_input) == expected

    def test_get_next_user_id(self):
        pass