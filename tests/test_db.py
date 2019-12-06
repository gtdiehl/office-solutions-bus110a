from app.database_module import Database
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

    @pytest.mark.parametrize("employee_id, first_name, last_name, email, password",
                             [(9999, 'Py', 'Tester', 'py.tester@gmail.com', 'py')])
    def test_insert_user_db(self, setup_db, employee_id, first_name, last_name, email, password):
        db = Database(setup_db)
        insert_statement = "INSERT INTO Employee (EmployeeID, FirstName, LastName, Email, Password) " + \
                           "VALUES (" + str(employee_id) + ",'" + first_name + "','" + last_name + "','" + email + \
                           "','" + password + "')"
        query_statement = "SELECT EXISTS(SELECT * FROM Employee WHERE EmployeeID is " + str(employee_id) + \
                          " AND FirstName is '" + first_name + "' AND LastName is '" + last_name + \
                          "' AND Email is '" + email + "' AND Password is '" + password + "')"
        insert_results = db.insert_user_db(insert_statement)
        query_results = db.query_user_db(query_statement)
        assert insert_results == True
        assert query_results[0] == 1

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
