# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:46:21 2019

@author: Admin
"""


def deleteuser(mydb):
    while True:
        
        del_email = input("\nPlease note that E-mail addresses are case-sensitive.\n"
                          "Enter an e-mail address to be deleted -- or press 'Enter' to return to the menu: ")
        if not del_email:
            print("\nNo user accounts were affected.  Returning to the previous menu.")
            return False
        results = mydb.query_user_db("SELECT EXISTS(SELECT * FROM Employee WHERE Email is ?)", (del_email, ))
        if results[0] == 1:
            condel_email = input("Please re-enter e-mail address to confirm deletion: ")
            userdeleted = mydb.delete_user_db("DELETE FROM Employee WHERE Email is ?", (condel_email, ))
            if userdeleted:
                print("\nUser %s has been deleted." % condel_email)
            return userdeleted
        else:
            print("\nYou have entered an e-mail address that is not in the database.  No user accounts were affected.")
            return False
       
        
           
            
                 
            
                         
