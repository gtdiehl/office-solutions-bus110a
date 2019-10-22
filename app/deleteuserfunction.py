# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:46:21 2019

@author: Admin
"""
import database


def deleteuser(mydb):
    while True:
        
        del_email = input("Enter email to delete: ")
        results = mydb.query_user_db("SELECT EXISTS(SELECT * FROM Employee WHERE Email is \'" +
                                       del_email + "\')")
        if results[0] == 1:
            print("Please re-enter email to confirm deletion")
            condel_email = input("To confirm deletion, re-enter email: " )
            
            
            userdeleted = mydb.delete_user_db("DELETE FROM Employee WHERE Email is +\'" + condel_email + 
                                              "\'")
            return userdeleted
        else:
            print("You have entered email that is not in the database, try again")
            return False
       
        
           
            
                 
            
                         
if __name__ == "__main__":
    mydb = database.Database()
    result = deleteuser(mydb)
    print("Result: " + str(result))