#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 18:35:22 2019

@author: joel
"""
import user_module
import report_module

class BestMenu:
    def __init__(self, myDB):
        self.myDB = myDB
        
    def createBestMenu(self):
        ans = True
        while(ans):
            ans = self._menuLoop(ans)
    
    def _menuLoop(self, ans):
          print("1. Report A")
          print("2. Report B")
          print("3. Register New User")
          print("4. Exit/Quit")
          ans=int(input("Please Select a Choice: "))
          if ans == "1":
              report_module.Report()
              print("\n Report A")
          elif ans == "2":
              report_module.Report()
              print("\n Report B")
          elif ans == "3":
              user_module.UserControl(self.myDB).addNewUser()
          elif ans =="4":
              print("\n Goodbye!")
              return False 
          elif ans =="":
              print("\n Invalid Choice, Enter 1-4")
          else:
              print("\n Invalid Choise, Enter 1-4")
              
          return True 
          