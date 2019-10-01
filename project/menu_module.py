import user_module
import report_module

class Menu:
    def __init__(self, myDB):
        self.myDB = myDB

    def createMenu(self):
        ans = True        
        while(ans):
            ans = self._menuLoop(ans)
    
    def _menuLoop(self, ans):
        print("""
        1. Run Report A
        2. Run Report B
        3. Register New User
        4. Exit/Quit
        """)
        ans=input("What would you like to do? ")
        if ans=="1":
            report_module.Report()
            print("\nReport A")
        elif ans=="2":
            report_module.Report()
            print("\n Report B")
        elif ans=="3":
            print("\n Add New User")
            user_module.UserControl(self.myDB).addNewUser()
        elif ans=="4":
            print("\n Goodbye") 
            return False
        elif ans=="":
            print("\n Not Valid Choice Try again")
        else:
            print("\n Not Valid Choice Try again")
    
        return True