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

    @pytest.mark.parametrize("test_input",
                             ["SELECT * FROM NoTable"])
    def test_query_exception(self, setup_db, test_input):
        test_db = Database(setup_db)
        with pytest.raises(Exception):
            assert test_db.query_user_db(test_input)

    @pytest.mark.parametrize("test_input,expected",
                             [("INSERT INTO Employee (EmployeeID, FirstName, LastName, Email, Password) " +
                              "VALUES (9999,'Py','Tester','py.tester@gmail.com','py')", True)
                              ])
    def test_insert_user_db(self, setup_db, test_input, expected):
        db = Database(setup_db)
        results = db.insert_user_db(test_input)
        assert results == expected

    @pytest.mark.parametrize("test_input",
                             [("INSERT INTO Employee (EmployeeID, FirstName, LastName, Email) " +
                              "VALUES (9999,'Py','Tester','py.tester@gmail.com','py')")
                              ])
    def test_insert_exception(self, setup_db, test_input):
        db = Database(setup_db)
        with pytest.raises(Exception):
            assert db.insert_user_db(test_input)

    @pytest.mark.parametrize("test_input,expected",
                             [("DELETE FROM Employee WHERE EMail is 'kk.chang@gmail.com'", False),
                              ("DELETE FROM Employee WHERE EMail is 'nora.chang@gmail.com'", True),
                              ("DELETE FROM Employee", True)])
    def test_delete_user_db(self, setup_db, test_input, expected):
        db = Database(setup_db)
        results = db.delete_user_db(test_input)
        assert results == expected
