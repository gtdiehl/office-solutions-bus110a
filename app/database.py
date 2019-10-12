import sqlite3


class Database:
    def __init__(self, _user_db_name='OS_Employee.db'):
        self._user_db_name = str(_user_db_name)

    def _connect_user_db(self):
        # Connect to the Database
        try:
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
        self.db_conn.close()

    def query_user_db(self, query_statement):
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

    def delete_user_db(self, delete):
        pass
