import re

class UserController:
    def __init__(self, myDB):
        self.myDB = myDB
    
    def _verifyUserName(self, inputText):
       # RegEx Search will return None if the string only contains letters
        # If Numbers, Special Characters, Spaces, etc... are found
        # function will return a fail message
        
        if((re.search(r'[^a-zA-Z]', inputText)) is None):
            
            return True
        else:
            return False
    
    def _verifyPassword(self, password):
        # Password can only consist of at least 8 characters
        # only limited to letters and numbers.
        if(re.match(r'[a-zA-Z0-9]{8,}', password) is not None):
            return True
        else:
            return False
    
    def _verifyEmailAddress(self, address):
        # RegEx will validate the E-Mail Address based on RFC 5322
        # If the e-mail address is not in the proper format the function
        # will return False
        if(re.search(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', address) is not None):
            return True
        else:
            return False
    
    def addNewUser(self):
        
        print("Enter new user information, all information is case-sensitive.")
        while(True):
            newFirstName = input("First Name: ")
            if(self._verifyUserName(newFirstName) == False):
                print("First name contains invalid characters. First name must only contain Alpabetic charaters, no Spaces, no Numbers, or no Special Characters are allow." +
                      "\nRe-enter the First Name")
                continue
            else:
                break
                
        while(True):
            newLastName = input("Last Name: ")
            if(self._verifyUserName(newLastName) == False):
                print("Last name contains invalid characters. Must only contain Alpabetic characters. Re-enter Last Name")
                continue
            else:
                break
    
        while(True):        
            newEmailAddress = input("E-Mail Address: ")
            if(self._verifyEmailAddress(newEmailAddress) == False):
                print("E-Mail Address is in invalid format. Re-enter valid E-Mail Address")
                continue
            else:
                break
    
        while(True):
            newUserPassword = input("Password: ")
            if(self._verifyPassword(newUserPassword) == False):
                print("Password does not meet requirements." +
                    "\nMust be at least 8 characters in length, only letters and numbers are allowed" + 
                    "\nRe-enter Password")
                continue
                
            newUserPasswordVerification = input("Re-Enter Password: ")
            if((newUserPassword == newUserPasswordVerification) == False):
                print("Passwords do not match. Re-enter password")
                continue

            else:
                break
        
        results = self.myDB.query_user_db("SELECT EXISTS(SELECT * FROM Employee WHERE Email is \'" + newEmailAddress + "\')")
        if(results[0] == 0):
            newUserID = self._getNextUserID()
            insertStatement = "INSERT INTO Employee (EmployeeID, FirstName, LastName, Email, Password) VALUES (" + str(newUserID) + ",'" + newFirstName + "','" + newLastName + "','" + newEmailAddress + "','" + newUserPassword + "')"
            if(self.myDB.insert_user_db(insertStatement)):
                print("\n New User was successfully added")
            else:
                print("\n[ERROR] New User was not added!")
        else:
            print("\n[ERROR] E-Mail address already register to another user")
            
    def _getNextUserID(self):
        userID = 0
        results = self.myDB.query_user_db("SELECT EmployeeID from Employee ORDER BY EmployeeID")
        userID = int(max(results)) + 1
            
        return userID