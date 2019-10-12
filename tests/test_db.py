from app.database import Database
import pytest


@pytest.mark.usefixtures("setup_db")
class TestDB:
    def test_db_connect(self, setup_db):
        test_db = Database(setup_db)
        assert test_db._connect_user_db() == True

    def test_db_disconnect(self, setup_db):
        pass

    @pytest.mark.parametrize("test_input,expected",
                             [("SELECT * FROM Employee", 9),
                              ("SELECT Email from Employee WHERE Email is 'nora.chang@gmail.com'", 1)])
    def test_query_user_db(self, setup_db, test_input, expected):
        test_db = Database(setup_db)
        results = test_db.query_user_db(test_input)
        assert len(results) == expected

    @pytest.mark.parametrize("test_input,expected",
                             [("INSERT INTO Employee (EmployeeID, FirstName, LastName, Email, Password) " +
                              "VALUES (9999,'Py','Tester','py.tester@gmail.com','py')", []),
                              ("INSERT INTO Employee (EmployeeID, FirstName, LastName, Email) " +
                              "VALUES (9999,'Py','Tester','py.tester@gmail.com','py')", None)
                              ])
    def test_insert_user_db(self, setup_db, test_input, expected):
        db = Database(setup_db)
        results = db.query_user_db(test_input)
        assert results == expected
