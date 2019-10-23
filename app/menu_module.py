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
        return ans
    
    def _menuLoop(self):
        print("----------[Main Menu]----------")
        print("" +
              "[1] Report Menu\n" +
              "[2] User Administration Menu\n" +
              "")
        menu_selection = input("Please enter an option [1-2, q to Quit] : ")
        if menu_selection == "1":
            pass
        elif menu_selection == "2":
            self._user_submenu_loop()
        elif menu_selection == "q" or menu_selection == "Q":
            print("\nGoodbye!")
            return False
        elif menu_selection == "":
            print("\nNot a valid choice. Please try again.")
        else:
            print("\nNot a valid choice. Please try again.")
        return True

    def _user_submenu_loop(self):
        while True:
            print("----------[User Administration Menu]----------")
            print("" +
                  "[1] Add New User\n" +
                  "[2] Delete Existing User\n" +
                  "")
            menu_selection = input("Please enter an option [1-2, r to Return to the Main Menu] : ")
            if menu_selection == "1":
                pass
            elif menu_selection == "2":
                deleteuserfunction.deleteuser(self.myDB)
            elif menu_selection == "r" or menu_selection == "R":
                break
            elif menu_selection == "":
                print("\nNot a valid choice. Please try again.")
            else:
                print("\nNot a valid choice. Please try again.")