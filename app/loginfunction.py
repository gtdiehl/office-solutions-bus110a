# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:28:15 2019

@author: Admin
"""

class login:
    def __init__(self, myDB):
        self.myDB = myDB
###The function above allows for connection to the database###
        
    def login(self):
        login_successful = False
        for i in range (3, 0, -1):
###The for loop starts at a range of 3 to 1. -1 subrtacts from 3 for each unsucessful attempt###
            
                email = input("Please enter email: ")
                password = input("Please enter password: ")
            
                results = self.myDB.query_user_db("SELECT EXISTS(SELECT * FROM Employee WHERE Email is \'" +
                                       email + "\' AND Password is \'" + 
                                       password + "\')")
                print("dvsdf: " + str(results))
                if results == [1]:
        
                    print("Login Sucessful ")
                    login_successful = True
                    break
                
        if login_successful == True:
            return True
        else:
            print("Contact admin")
            return False
            
        
        
            
                   
###If attempt is ###
      
                
       
        


