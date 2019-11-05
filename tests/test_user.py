from app.database import Database
from app.Add_User import UserController
from tests.input_test_base import set_keyboard_input, get_display_output
import pytest


@pytest.mark.usefixtures("setup_db")
class TestUser:
    @pytest.mark.parametrize("test_input_first_name, test_input_last_name, test_input_email, test_input_password, "
                             "expected", [("Greg", "Thomas", "greg@gmail.com", "greggreg", 1)])
    def test_add_user_success(self, setup_db, test_input_first_name, test_input_last_name, test_input_email,
                              test_input_password, expected):
        test_db = Database(setup_db)
        user = UserController(test_db)
        set_keyboard_input([test_input_first_name, test_input_last_name, test_input_email, test_input_password,
                            test_input_password])
        user.addNewUser()
        output = get_display_output()
        assert output == ["Enter new user information, all information is case-sensitive.", "First Name: ",
                          "Last Name: ", "E-Mail Address: ", "Password: ", "Re-Enter Password: ",
                          "\n New User was successfully added"]
        result = test_db.query_user_db("SELECT EXISTS(SELECT * FROM Employee WHERE FirstName is '%s' AND LastName is "
                                       "'%s' AND Email is '%s' AND Password is '%s')" %
                                       (test_input_first_name, test_input_last_name, test_input_email,
                                        test_input_password))
        assert result[0] == expected

    @pytest.mark.parametrize("test_input_bad_first_name, test_input_good_first_name, test_input_last_name, "
                             "test_input_email, test_input_password, expected",
                             [("", "Greg", "Thomas", "greg@gmail.com", "greggreg", 1)])
    def test_add_user_blank_first_name(self, setup_db, test_input_bad_first_name, test_input_good_first_name, test_input_last_name, test_input_email,
                                       test_input_password, expected):
        test_db = Database(setup_db)
        user = UserController(test_db)
        set_keyboard_input([test_input_bad_first_name, test_input_good_first_name, test_input_last_name,
                            test_input_email, test_input_password, test_input_password])
        user.addNewUser()
        output = get_display_output()
        assert output == ["Enter new user information, all information is case-sensitive.", "First Name: ",
                          "First name can not be blank.  Please enter a first name.", "First Name: ",
                          "Last Name: ", "E-Mail Address: ", "Password: ", "Re-Enter Password: ",
                          "\n New User was successfully added"]
        result = test_db.query_user_db("SELECT EXISTS(SELECT * FROM Employee WHERE FirstName is '%s' AND LastName is "
                                       "'%s' AND Email is '%s' AND Password is '%s')" %
                                       (test_input_good_first_name, test_input_last_name, test_input_email,
                                        test_input_password))
        assert result[0] == expected

    def test_add_user_invalid_first_name(self):
        pass

    def test_add_user_blank_last_name(self):
        pass

    def test_add_user_invalid_last_name(self):
        pass

    def test_add_user_blank_email(self):
        pass

    def test_add_user_blank_password(self):
        pass

    def test_add_user_invalid_password_length(self):
        pass

    def test_add_user_invalid_password(self):
        pass

    def test_add_user_blank_re_password(self):
        pass

    def test_add_user_invalid_re_password_length(self):
        pass

    def test_add_user_invalid_re_password(self):
        pass

    def test_add_user_already_exists(self):
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