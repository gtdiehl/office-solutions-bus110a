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
                self.prompt_for_filter(1)
            elif menu_selection == "2":
                self.prompt_for_filter(2)
            elif menu_selection == "3":
                self.prompt_for_filter(3)
            elif menu_selection == "4":
                self.prompt_for_filter(4)
            elif menu_selection == "5":
                self.prompt_for_filter(5)
            elif menu_selection == "6":
                self.prompt_for_filter(6)
            elif menu_selection == "r" or menu_selection == "R":
                break
            elif menu_selection == "":
                print("\nNot a valid choice. Please try again.")
            else:
                print("\nNot a valid choice. Please try again.")

    def prompt_for_filter(self, report_num):
        report_range = []

        report_type = input("Do you want the report by Quarter or Month? [Q - Quarterly, M - Monthly]: ")

        if report_type == 'q' or report_type == 'Q':
            quarter = int(input("Which Quarter? [1 - 4]: "))
            year = int(input("Which Year? [Enter YYYY format]: "))
            report_range = self.quarter_to_months(quarter, year)
            
        elif report_type == 'm' or report_type == 'M':
            month = int(input("Which Month? [1 - 12]: "))
            year = int(input("Which Year? [YYYY format]: "))
            report_range.append(month)
            report_range.append(year)
            report_range.append(month)
            report_range.append(year)

        if report_num == 1:
            reports.top_ten_profits(report_range[0], report_range[1], report_range[2], report_range[3])
        elif report_num == 2:
            reports.least_ten_profits(report_range[0], report_range[1], report_range[2], report_range[3])
        elif report_num == 3:
            pass
        elif report_num == 4:
            pass
        elif report_num == 5:
            pass
        elif report_num == 6:
            pass
        else:
            print("[ERROR] Report does not exist!")


    def quarter_to_months(self, quarter, year):          
        report_range = []
        starting_month = (quarter * 3) - 2
        report_range.append(starting_month)
        report_range.append(year)        
        
        ending_month = quarter * 3
        report_range.append(ending_month)
        report_range.append(year)
        
        return report_range        
    
     
