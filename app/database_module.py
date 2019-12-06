import os
import sqlite3


class Database:
    """
    The Database object

    Args:
        user_db_name (str): This argument is used to specify the location of the Employee Database file

    Attributes:
        user_db_name (str): This is where we store user_db_name

    """
    def __init__(self, user_db_name=(os.path.join(os.path.dirname(__file__), 'OS_Employee.db'))):
        self._user_db_name = str(user_db_name)

    def _connect_user_db(self):
        """
        Helper method to connect to the SQLite3 database.
        This is a private (internal) method NOT to be called directly.
        Please use a method such as 'query_user_db' method
        """
        try:
            # Connect to the Database file
            self.db_conn = sqlite3.connect(self._user_db_name)

            # This statement makes the ResultSet returned as a List rather than a Tuple
            # that needs to be parsed
            self.db_conn.row_factory = lambda cursor, row: row[0]

            if type(self.db_conn) is sqlite3.Connection:
                # Make sure the connection to the db file is valid.
                return True
            else:
                # Return False if the self.db_conn object does not make a connection to the db.
                return False

        except sqlite3.Error as e:
            print(e)
            # Return False if any errors occur while connecting to the db.
            return False

    def _disconnect_user_db(self):
        """
        Helper method to connect to the SQLite3 database.
        This is a private (internal) method NOT to be called directly.
        Please use a method such as 'query_user_db' method
        """
        # Closes the database connection.
        self.db_conn.close()

    def _query_statement(self, *args, **kwargs):
        """
        Helper method to query the SQLite3 database.
        This method is used to reduce redundant code.
        This is a private (internal) method NOT to be called directly.
        Please use a method such as 'query_user_db' method
        """
        results = []
        try:
            # Connects to the database
            self._connect_user_db()
            # Cursor object is required to fetch data from the database.
            cur = self.db_conn.cursor()
            # Executes the SQL statement against the database.
            cur.execute(*args, **kwargs)
            # All records are returned from the database to the results object.
            results = cur.fetchall()
            # Disconnects from the database.
            self._disconnect_user_db()
        except sqlite3.Error as e:
            print("[ERROR] " + str(e))

        # Returns the result object.
        return results

    def _commit_statement(self, *args, **kwargs):
        """
        Helper method to run statements against the SQLite3 database that require a commit.
        This method is used to reduce redundant code.
        This is a private (internal) method NOT to be called directly.
        Please use a method such as 'insert_user_db' method
        """
        try:
            # Connects to the database
            self._connect_user_db()
            # Cursor object is required to insert data from the database.
            cur = self.db_conn.cursor()
            # Executes the SQL statement against the database.
            cur.execute(*args, **kwargs)
            # Commits the data to the database.  It is now saved.
            self.db_conn.commit()
            total_changes = self.db_conn.total_changes
            # Disconnects from the database.
            self._disconnect_user_db()
        except sqlite3.Error as e:
            print("[ERROR] " + str(e))
            return False

        # Returns true if the insert was a success.  Success is when more than zero changes occur.
        if total_changes > 0:
            return True
        else:
            return False

    def query_user_db(self, *args, **kwargs):
        """
        Queries the Employee database.
        Will only return the first column from the SQL Select statement.
        For example 'SELECT * FROM Employee' will return only a list of Employee IDs.
        TODO: Make the method return all columns OR create a different method to return all columns.

        Args:
            args
            kwargs

        Raises:
            sqlite3.Error: Catch all for all SQLite3 exception types

        Returns:
            results: List type object with the database result set
        """
        return self._query_statement(*args, **kwargs)

    def insert_user_db(self, *args, **kwargs):
        """
        Inserts data into the Employee database

        Args:
            args
            kwargs

        Raises:
            sqlite3.Error: Catch all for all SQLite3 exception types

        Returns:
            bool: The return value.  True for success, False otherwise.
        """
        return self._commit_statement(*args, **kwargs)

    def delete_user_db(self, *args, **kwargs):
        """
        Deletes data from the Employee database

        Args:
            args
            kwargs

        Raises:
            sqlite3.Error: Catch all for all SQLite3 exception types

        Returns:
            bool: The return value.  True for success, False otherwise.
        """
        return self._commit_statement(*args, **kwargs)
