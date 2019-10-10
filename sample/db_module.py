import sqlite3

class Database:
    def __init__(self):
        self._dbName = 'OS_Employee.db'

    def _connectDB(self):
        # Connect to the Database
        try:
            self.dbConn = sqlite3.connect(self._dbName)
            
            # This statement makes the ResultSet returned as a List rather than a Tuple
            # that needs to be parsed
            self.dbConn.row_factory = lambda cursor, row: row[0]
            
        except sqlite3.Error as e:
            print(e)
    
    def _disconnectDB(self):
        self.dbConn.close()
    
    def queryDB(self, queryStatement):
        try:
            self._connectDB()
            cur = self.dbConn.cursor()
            cur.execute(queryStatement)
            results = cur.fetchall()
            self._disconnectDB()
        except sqlite3.Error as e:
            print(e)
        return results
    
    def insertDB(self, insertStatement):
        try:
            self._connectDB()
            cur = self.dbConn.cursor()
            cur.execute(insertStatement)
            self.dbConn.commit()
            self._disconnectDB()
            return True
        except sqlite3.Error as e:
            print(e)
            return False