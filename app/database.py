import sqlite3


class Database:
    """
    The Database object

    Args:
        user_db_name (str): This argument is used to specify the location of the Employee Database file

    Attributes:
        user_db_name (str): This is where we store user_db_name

    """
    def __init__(self, user_db_name='OS_Employee.db'):
        self._user_db_name = str(user_db_name)

    def _connect_user_db(self):
        """
        Method to connect to the SQLite3 database.
        This is a private (internal) method NOT to be called directly.
        Please use a helper method such as 'query_user_db' method
        """
        try:
            ''' Connect to the Database'''
            self.db_conn = sqlite3.connect(self._user_db_name)

            # This statement makes the ResultSet returned as a List rather than a Tuple
            # that needs to be parsed
            self.db_conn.row_factory = lambda cursor, row: row[0]

            if self.db_conn is not None:
                return True
            else:
                return False

        except sqlite3.Error as e:
            print(e)
            return False

    def _disconnect_user_db(self):
        """
        Method to connect to the SQLite3 database.
        This is a private (internal) method NOT to be called directly.
        Please use a helper method such as 'query_user_db' method
        """
        self.db_conn.close()

    def query_user_db(self, query_statement):
        """
        Queries the Employee database

        Args:
            query_statement (str): String should conform the the standard SQL format

        Raises:
            sqlite3.Error: Catch all for all SQLite3 exception types

        Returns:
            results: List type object with the database result set
        """
        try:
            self._connect_user_db()
            cur = self.db_conn.cursor()
            cur.execute(query_statement)
            results = cur.fetchall()
            self._disconnect_user_db()
        except sqlite3.Error as e:
            results = None
            print(e)
        return results

    def insert_user_db(self, insert_statement):
        """
        Inserts data into the Employee database

        Args:
            insert_statement (str): String should conform the the standard SQL format

        Raises:
            sqlite3.Error: Catch all for all SQLite3 exception types

        Returns:
            bool: The return value.  True for success, False otherwise.
        """
        try:
            self._connect_user_db()
            cur = self.db_conn.cursor()
            cur.execute(insert_statement)
            self.db_conn.commit()
            self._disconnect_user_db()
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def delete_user_db(self, delete_user_email):
        """
        Deletes a user from the Employee database

        Args:
            delete_user_email (str): The specified user's e-mail address will be to query the database
                                     and remove that user from the database.

        Raises:
            sqlite3.Error: Catch all for all SQLite3 exception types

        Returns:
            bool: The return value.  True for success, False otherwise.
        """
        pass
