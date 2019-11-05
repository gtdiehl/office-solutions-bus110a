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
            print()
            print("" +
                  "[1] Most Profitable Product Report\n" +
                  "[2] Least Profitable Product Report\n" +
                  "[3] Most Frequent Buyerst\n" +
                  "[4] Most Discounted Products\n" +
                  "[5] "                      "\n" +
                  "[6] "                      "\n" +
                  "")
            menu_selection = input("Please enter an option [1-2, r to Return to the Main Menu] : ")
            if menu_selection == "1":
                self.prompt_for_filter_mostprofit()
            elif menu_selection == "2":
                self.prompt_for_filter_leastprofit()
            elif menu_selection == "3":
                self.prompt_for_filter_info()
            elif menu_selection == "4":
                self.prompt_for_filter_info()
            elif menu_selection == "5":
                self.prompt_for_filter_info()
            elif menu_selection == "6":
                self.prompt_for_filter_info()
            elif menu_selection == "r" or menu_selection == "R":
                break
            elif menu_selection == "":
                print("\nNot a valid choice. Please try again.")
            else:
                print("\nNot a valid choice. Please try again.")
                
    def prompt_for_filter_mostprofit(self):
        fromdate_entry = input('Enter a date in YYYY-MM-DD format')
        year, month, day = map(int, fromdate_entry.split('-'))
     
        
        
        todate_entry = input('Enter a date in YYYY-MM-DD format')
        year, month, day = map(int, todate_entry.split('-'))
       
       
       
        
        '''
        Run report function using the above inputs
        '''
        reports.top_ten_profits(fromdate_entry, todate_entry)
        print("Report from period %d/%d to %d/%d" % (fromdate_entry, todate_entry))
    
    def prompt_for_filter_leastprofit(self):
        from_month = int(input("What Month?"))
        from_year = int(input("What Year?"))
        to_month = int(input("What Month?"))
        to_year = int(input("What Year?"))
        
        '''
        Run report function using the above inputs
        '''
        reports.least_ten_profits(from_month, from_year, to_month, to_year)
        print("Report from period %d/%d to %d/%d" % (from_month, from_year, to_month, to_year))

   