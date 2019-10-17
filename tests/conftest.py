import pytest
import sqlite3


@pytest.fixture(scope="function")
def setup_db(tmpdir_factory):
    file = tmpdir_factory.mktemp("data").join("OS_Employee.db")
    conn = sqlite3.connect(str(file))
    conn.execute("CREATE TABLE Employee (EmployeeID, FirstName, LastName, Email, Password)")
    conn.execute("INSERT INTO \"Employee\" VALUES (\'1005\',\'Nora\',\'Chang\',\'nora.chang@gmail.com\',\'nora\');")
    conn.execute("INSERT INTO \"Employee\" VALUES (\'1006\',\'Elanor\',\'White\',\'elanor.white@gmail.com\'" +
                 ",\'elanor\');")
    conn.execute("INSERT INTO \"Employee\" VALUES (\'1007\',\'Charles\',\'Lopez\',\'charles.lopez@gmail.com\'," +
                 "\'charles\');")
    conn.execute("INSERT INTO \"Employee\" VALUES (\'1009\',\'Emma\',\'Moran\',\'emma.moran@gmail.com\',\'emma\');")
    conn.execute("INSERT INTO \"Employee\" VALUES (\'1008\',\'Patrick\',\'Harris\',\'patrick.harris@gmail.com\'," +
                 "\'patrick\');")
    conn.execute("INSERT INTO \"Employee\" VALUES (\'1003\',\'William\',\'Jones\',\'william.jones@gmail.com\'," +
                 "\'william\');")
    conn.execute("INSERT INTO \"Employee\" VALUES (\'1004\',\'Jennifer\',\'Lee\',\'jennifer.lee@gmail.com\'," +
                 "\'jennifer\');")
    conn.execute("INSERT INTO \"Employee\" VALUES (\'1002\',\'Belle\',\'Nguyen\',\'belle.nguyen@gmail.com\'," +
                 "\'belle\');")
    conn.execute("INSERT INTO \"Employee\" VALUES (\'1001\',\'Bob\',\'Moore\',\'bob.moore@gmail.com\',\'bob\');")
    conn.commit()
    yield file
    conn.close()
