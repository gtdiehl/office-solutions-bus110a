# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:28:15 2019

@author: Admin
"""


class login:
    def __init__(self, myDB):
        # The function above allows for connection to the database
        self.myDB = myDB
        
    def login(self):
        login_successful = False
        # The for loop starts at a range of 3 to 1. -1 subtracts from 3 for each unsuccessful attempt
        for i in range(3, 0, -1):

            email = input("Please enter email: ")
            password = input("Please enter password: ")

            results = self.myDB.query_user_db("SELECT EXISTS(SELECT * FROM Employee WHERE Email is ? AND "
                                              "Password is ?)", (email, password))

            if results == [1]:
                print("\nLogin Successful")
                login_successful = True
                break
            else:
                if i > 1:
                    print("Unsuccessful login attempt.  Please try again. Note that e-mail addresses and passwords are "
                          "case-sensitive.")
                else:
                    print("Unsuccessful login attempt. Note that e-mail addresses and passwords are case-sensitive.")
                
        if login_successful:
            return True
        else:
            print("Please contact your administrator for your login credentials.")
            return False
