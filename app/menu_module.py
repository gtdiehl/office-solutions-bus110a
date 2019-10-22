#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 18:35:22 2019

@author: joel
"""

import deleteuserfunction

class BestMenu:
    def __init__(self, myDB):
        self.myDB = myDB
        
    def createBestMenu(self):
        ans = True
        while ans:
            ans = self._menuLoop()
    
    def _menuLoop(self):
        print("----------[Main Menu]----------")
        print("" +
              "[1] Report Menu\n" +
              "[2] User Administration Menu\n" +
              "")
        ans = input("Please enter an option [1-2, q to Quit] : ")
        if ans == "1":
            pass
        elif ans == "2":
            self._user_submenu_loop()
        elif ans == "q" or ans == "Q":
            print("\nGoodbye!")
            return False
        elif ans == "":
            print("\nNot a valid choice. Please try again.")
        else:
            print("\nNot a valid choice. Please try again.")
        '''
          print("1. Report A")
          print("2. Report B")
          print("3. Register New User")
          print("4. Exit/Quit")
          ans=input("Please Select a Choice: ")
          if ans == "1":
              print("\n Report A")
          elif ans == "2":
              print("\n Report B")
          elif ans == "3":
              pass
          elif ans =="4":
              print("\n Goodbye!")
              return False 
          elif ans =="":
              print("\n Invalid Choice, Enter 1-4")
          else:
              print("\n Invalid Choise, Enter 1-4")
        '''
        return True

    def _user_submenu_loop(self):
        print("----------[User Administration Menu]----------")
        print("" +
              "[1] Add New User\n" +
              "[2] Delete Existing User\n" +
              "")
        ans = input("Please enter an option [1-2, r to Return to the Main Menu] : ")
        if ans == "1":
            pass
        elif ans == "2":
            deleteuserfunction.deleteuser(self.myDB)
        elif ans == "r" or ans == "R":
            self._menuLoop()
        elif ans == "":
            print("\nNot a valid choice. Please try again.")
        else:
            print("\nNot a valid choice. Please try again.")