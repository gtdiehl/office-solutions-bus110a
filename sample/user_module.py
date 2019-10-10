import re

class UserControl:
    def __init__(self, myDB):
        self.myDB = myDB
    
    def _validateUserNameInput(self, inputText):
        # RegEx Search will return None if the string only contains letters
        # Otherwise if Numbers, Special Characters, Spaces, etc... are found
        # the Search function will return something telling us to fail the
        # validation of the text.
        if((re.search(r'[^a-zA-Z]', inputText)) is None):
            return True
        else:
            return False
    
    def _validatePassword(self, password):
        # Password can only consist of ASCII visible characters
        # Spaces are prevented and will cause the function to return False
        if(re.search(r'^[\x21-\x7E]+$', password) is not None):
            return True
        else:
            return False
    
    def _validateEmailAddress(self, address):
        # RegEx will validate the E-Mail Address based on RFC 5322
        # If the e-mail address is not in the proper format the function
        # will return False
        if(re.search(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', address) is not None):
            return True
        else:
            return False
    
    def addNewUser(self):
        
        print("Please enter in the new user information")
        while(True):
            newFirstName = input("First Name: ")
            if(self._validateUserNameInput(newFirstName) == False):
                print("First name contains invalid characters. Can only contain Alpabetic charaters, No Spaces, No Numbers, or No Special Characters." +
                      "\nPlease re-enter the First Name")
                continue
            else:
                break
                
        while(True):
            newLastName = input("Last Name: ")
            if(self._validateUserNameInput(newLastName) == False):
                print("Last name contains invalid characters. Please re-enter the Last Name")
                continue
            else:
                break
    
        while(True):        
            newEmailAddress = input("E-Mail Address: ")
            if(self._validateEmailAddress(newEmailAddress) == False):
                print("E-Mail Address contains invalid characters. Please re-enter the E-Mail Address")
                continue
            else:
                break
    
        while(True):
            newUserPassword = input("Password: ")
            newUserPasswordReEnter = input("Re-Enter Password: ")
            if((newUserPassword == newUserPasswordReEnter) == False):
                print("Passwords do not match.  Please re-enter the Passwords.")
                continue
            elif(self._validatePassword(newUserPassword) == False):
                print("Password contains invalid characters. Please re-enter the Password")
                continue
            else:
                break
        
        results = self.myDB.queryDB("SELECT EXISTS(SELECT * FROM Employee WHERE Email is \'" + 
                                                   newEmailAddress + "\')")
        if(results[0] == 0):
            newUserID = self._getNextUserID()
            insertStatement = "INSERT INTO Employee (EmployeeID, FirstName, LastName, Email, Password) VALUES (" + str(newUserID) + ",'" + newFirstName + "','" + newLastName + "','" + newEmailAddress + "','" + newUserPassword + "')"
            if(self.myDB.insertDB(insertStatement)):
                print("\nNew User was successfully added")
            else:
                print("\n[ERROR] New User was not added!")
        else:
            print("\n[ERROR] New User E-Mail address already exists!")
            
    def _getNextUserID(self):
        userID = 0
        results = self.myDB.queryDB("SELECT EmployeeID from Employee ORDER BY EmployeeID")
        userID = int(max(results)) + 1
            
        return userID