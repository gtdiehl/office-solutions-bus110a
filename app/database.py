import sqlite3

class Database:
    def __init__(self):
        self._UserDBName = 'OS_Employee.db'

    def _connectUserDB(self):
        # Connect to the Database
        try:
            self.dbConn = sqlite3.connect(self._UserDBName)

            # This statement makes the ResultSet returned as a List rather than a Tuple
            # that needs to be parsed
            self.dbConn.row_factory = lambda cursor, row: row[0]

            if self.dbConn != None:
                return True
            else:
                return False

        except sqlite3.Error as e:
            print(e)

    def _disconnectUserDB(self):
        self.dbConn.close()

    def queryUserDB(self, queryStatement):
        try:
            self._connectUserDB()
            cur = self.dbConn.cursor()
            cur.execute(queryStatement)
            results = cur.fetchall()
            self._disconnectUserDB()
        except sqlite3.Error as e:
            print(e)
        return results

    def insertUserDB(self, insertStatement):
        try:
            self._connectUserDB()
            cur = self.dbConn.cursor()
            cur.execute(insertStatement)
            self.dbConn.commit()
            self._disconnectUserDB()
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def deleteUserDB(self, delete):
        pass