import re
from email_validator import validate_email, EmailNotValidError


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
        # Limited to only letters and numbers.
        string = re.search(r'[^a-zA-Z0-9.]', password)
        if not bool(string):
            return True
        else:
            return False
    
    def _verifyEmailAddress(self, address):
        # RegEx will validate the E-Mail Address based on RFC 5322
        # If the e-mail address is not in the proper format the function
        # will return False
        if re.search(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', address) is not None:
            pass
        else:
            print("The e-mail address must be in user@domain.com format. Please enter a valid e-Mail address.")
            return False

        try:
            v = validate_email(address)  # validate and get info
            email = v["email"]  # replace with normalized form
            return True
        except EmailNotValidError as e:
            # email is not valid, exception message is human-readable
            print(str(e) + " Please enter in a valid domain name.")
            return False

    def addNewUser(self):
        
        print("Enter new user information, all information is case-sensitive.")
        while(True):
            newFirstName = input("First Name: ")
            if newFirstName is "":
                print("First name can not be blank.  Please enter a first name.")
                continue
            if not self._verifyUserName(newFirstName):
                print("First name contains invalid characters. First name must only contain Alphabetic characters, "
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
                continue
            else:
                break
    
        while True:
            newUserPassword = input("Password: ")
            if newUserPassword is "":
                print("Password can not be blank. Please enter a password with only letters and numbers.")
                continue
            if len(newUserPassword) < 8 or len(newUserPassword) > 12:
                print("Password can only have a minimum of 8 characters to a maximum of 12 characters.")
                continue
            if not self._verifyPassword(newUserPassword):
                print("Password does not meet requirements. Password contains invalid characters. Please "
                      "enter a password with only letters and numbers.")
                continue
                
            newUserPasswordVerification = input("Re-Enter Password: ")
            if newUserPasswordVerification is "":
                print("Password can not be blank. Please enter a password with only letters and numbers.")
                continue
            if len(newUserPasswordVerification) < 8 or len(newUserPasswordVerification) > 12:
                print("Password can only have a minimum of 8 characters to a maximum of 12 characters.")
                continue
            if not self._verifyPassword(newUserPasswordVerification):
                print("Password does not meet requirements. Password contains invalid characters. Please"
                      "enter a password with only letters and numbers.")
                continue
            if not (newUserPassword == newUserPasswordVerification):
                print("Passwords do not match. Re-enter password")
                continue
            else:
                break
        
        results = self.myDB.query_user_db("SELECT EXISTS(SELECT * FROM Employee WHERE Email is ?)", (newEmailAddress, ))
        if results[0] == 0:
            newUserID = self._getNextUserID()
            if self.myDB.insert_user_db("INSERT INTO Employee (EmployeeID, FirstName, LastName, Email, Password) "
                                        "VALUES (?, ?, ?, ?, ?)", (newUserID, newFirstName, newLastName, newEmailAddress,
                                                                   newUserPassword)):
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
