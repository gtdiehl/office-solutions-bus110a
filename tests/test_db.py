from app.database import Database
import pytest


def test_db_connect():
    db = Database()
    assert db._connect_user_db() == True


def test_db_disconnect():
    pass


@pytest.mark.parametrize("test_input,expected",
                         [("SELECT * FROM Employee", 9),
                          ("SELECT Email from Employee WHERE Email is 'nora.chang@gmail.com'", 1)])
def test_query_user_db(test_input, expected):
    db = Database()
    results = db.query_user_db(test_input)
    assert len(results) == expected


@pytest.mark.parametrize("test_input,expected",
                        [("INSERT INTO Employee (EmployeeID, FirstName, LastName, Email, Password) " +
                          "VALUES (9999,'Py','Tester','py.tester@gmail.com','py')", []),
                         ("INSERT INTO Employee (EmployeeID, FirstName, LastName, Email) " +
                          "VALUES (9999,'Py','Tester','py.tester@gmail.com','py')", None)
                         ])
def test_insert_user_db(test_input, expected):
    db = Database()
    results = db.query_user_db(test_input)
    assert results == expected
