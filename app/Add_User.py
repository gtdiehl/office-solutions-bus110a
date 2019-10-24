#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:33:07 2019

@author: joel
"""

def addNewUser(self):
    print("Please Enter New User Information")
    while (True):
        newFirstName = input("Enter First Name: ")
        if(self._ValidateUserNameInput(newFirstName) == False):
            print("First name contains invalid characters. Use Alphabetic characters." + "\nEnter First Name: ")
            continue
        else:
            break
    while (True):
        newLastName = input("Enter Last Name: ")
        if(self._ValidateUserNameInput(newLastName) == False):
            print("Last name contains invalid characters. Only use Alphabetic Characters" + "\nEnter Last Name: ")
            continue
        else:
            break
    while (True):
        newEmail = input("Enter E-Mail Address: ")
        if(self._ValidateEmailInput(newEmail) == False):
            print("E-Mail contains invalid characters." + "\nEnter E-Mail: ")
            continue
        else:
<<<<<<< HEAD
            break
    while (True):
        newUserPass = input("Enter Password: ")
        newUserPassRe = input("Re-Enter Password: ")
        if((newUserPass == newUserPassre) == False):
            print("Password contains invalid characters." + "\Re-Enter Password: ")
            continue
        else:
            break
   results = self.myDB ("SELECT EXISTS(SELECT * FROM Employee WHERE Email is \'" +
                                   email + "\' AND Password is \'" +
                                   password + "\')")
      if(results[0] == 0):
          newUserID = self._getNextUserID()
          insertStatement = "Insert INTO employee VALUES ( EmployeeID, FirstName, LastName, Email, Password) VALUES (" + str(newUserID) + ",'" + newFirstName + "','" + newLastName + "','" + newEmail + "','" + newUserPass + "')"
          if (self.myDB.insertDB(insertStatement)):
              print("New User was successfully added")
          else:
              print("[ERROR] New user was not added")
              
    
=======
            return False
    
    def addNewUser(self):
        
        print("Enter new user information")
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
>>>>>>> ebb18bbf9231f983abccef64e94a713d6b0bac92
