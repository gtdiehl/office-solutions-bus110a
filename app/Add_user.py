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
              
    