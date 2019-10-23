import re


class UserController:
    def __init__(self, myDB):
        self.myDB = myDB
    
    def _verifyUserName(self, inputText):
        # RegEx Search will return None if the string only contains letters
        # If Numbers, Special Characters, Spaces, etc... are found
        # function will return a fail message
        
        if (re.search(r'[^a-zA-Z]', inputText)) is None:
            
            return True
        else:
            return False
    
    def _verifyPassword(self, password):
        # Password can only consist of at least 8 characters
        # only limited to letters and numbers.
        if re.match(r'[a-zA-Z0-9]{8,}', password) is not None:
            return True
        else:
            return False
    
    def _verifyEmailAddress(self, address):
        # RegEx will validate the E-Mail Address based on RFC 5322
        # If the e-mail address is not in the proper format the function
        # will return False
        if re.search(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', address) is not None:
            return True
        else:
            return False
    
    def addNewUser(self):
        
        print("Enter new user information, all information is case-sensitive.")
        while(True):
            newFirstName = input("First Name: ")
            if newFirstName is "":
                print("First name can not be blank.  Please enter a first name.")
                continue
            if not self._verifyUserName(newFirstName):
                print("First name contains invalid characters. First name must only contain Alpabetic charaters, "
                      "no Spaces, no Numbers, or no Special Characters are allow." +
                      "\nPlease ee-enter a first name")
                continue
            else:
                break
                
        while True:
            newLastName = input("Last Name: ")
            if newLastName is "":
                print("Last name can not be blank.  Please enter a last name.")
                continue
            if not self._verifyUserName(newLastName):
                print("Last name contains invalid characters. Must only contain Alphabetic characters. "
                      "Re-enter Last Name")
                continue
            else:
                break
    
        while True:
            newEmailAddress = input("E-Mail Address: ")
            if newEmailAddress is "":
                print("E-Mail address can not be blank.  Please enter an e-mail address.")
                continue
            if not self._verifyEmailAddress(newEmailAddress):
                print("The e-mail address must be in user@domain.com format. Please enter a valid e-Mail address.")
                continue
            else:
                break
    
        while True:
            newUserPassword = input("Password: ")
            if newUserPassword is "":
                print("Password can not be blank.  Please enter a password with at least 8 characters in length, "
                      "only letters and numbers are allowed")
                continue
            if not self._verifyPassword(newUserPassword):
                print("Password does not meet requirements." +
                      "\nMust be at least 8 characters in length, only letters and numbers are allowed" +
                      "\nRe-enter Password")
                continue
                
            newUserPasswordVerification = input("Re-Enter Password: ")
            if not (newUserPassword == newUserPasswordVerification):
                print("Passwords do not match. Re-enter password")
                continue
            else:
                break
        
        results = self.myDB.query_user_db("SELECT EXISTS(SELECT * FROM Employee WHERE Email is \'" +
                                          newEmailAddress + "\')")
        if results[0] == 0:
            newUserID = self._getNextUserID()
            insertStatement = "INSERT INTO Employee (EmployeeID, FirstName, LastName, Email, Password) VALUES (" + \
                              str(newUserID) + ",'" + newFirstName + "','" + newLastName + "','" + newEmailAddress + \
                              "','" + newUserPassword + "')"
            if self.myDB.insert_user_db(insertStatement):
                print("\n New User was successfully added")
            else:
                print("\n[ERROR] New User was not added!")
        else:
            print("\n[ERROR] New User was not added.  E-Mail address is already registered to another user.")
            
    def _getNextUserID(self):
        userID = 0
        results = self.myDB.query_user_db("SELECT EmployeeID from Employee ORDER BY EmployeeID")
        userID = int(max(results)) + 1
            
        return userID