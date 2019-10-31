#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 18:35:22 2019

@author: joel
"""

import deleteuserfunction
import Add_User
import reports


class BestMenu:
    def __init__(self, myDB):
        self.myDB = myDB
        
    def createBestMenu(self):
        ans = True
        while ans:
            ans = self._menuLoop()
        return ans
    
    def _menuLoop(self):
        print("\n----------[Main Menu]----------")
        print("" +
              "[1] Report Menu\n" +
              "[2] User Administration Menu\n" +
              "")
        menu_selection = input("Please enter an option [1-2, q to Quit] : ")
        if menu_selection == "1":
            self._report_submenu_loop()
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
            print("\n----------[User Administration Menu]----------")
            print("" +
                  "[1] Add New User\n" +
                  "[2] Delete Existing User\n" +
                  "")
            menu_selection = input("Please enter an option [1-2, r to Return to the Main Menu] : ")
            if menu_selection == "1":
                Add_User.UserController(self.myDB).addNewUser()
            elif menu_selection == "2":
                deleteuserfunction.deleteuser(self.myDB)
            elif menu_selection == "r" or menu_selection == "R":
                break
            elif menu_selection == "":
                print("\nNot a valid choice. Please try again.")
            else:
                print("\nNot a valid choice. Please try again.")
                
    def _report_submenu_loop(self):
        while True:
            print("\n----------[Report Menu]----------")
            print("" +
                  "[1] Run Most Profitable Product Report\n" +
                  "[2] Run Least Profitable Product Report\n" +
                  "")
            menu_selection = input("Please enter an option [1-2, r to Return to the Main Menu] : ")
            if menu_selection == "1":
                self.prompt_for_filter_info()
            elif menu_selection == "2":
                self.prompt_for_filter_info()
            elif menu_selection == "r" or menu_selection == "R":
                break
            elif menu_selection == "":
                print("\nNot a valid choice. Please try again.")
            else:
                print("\nNot a valid choice. Please try again.")
                
    def prompt_for_filter_info(self):
        month = input("What Month?")
        year = input("What Year?")
        
        '''
        Run report function using the above inputs
        '''
        reports.top_ten_profits(month, year)
        print("Running report for period %s/%s" % (month, year))