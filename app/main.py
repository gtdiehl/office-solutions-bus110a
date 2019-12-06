import Add_User
import database_module
import login_module
import menu_module


class Main:

    APP_VERSION = 1.0
    
    def __init__(self):
        self.mydb = database_module.Database()
        self.mylogin = login_module.Login(self.mydb)        
    
    def run(self):
        ans = True
        while ans:
            ans = self._menuloop()


    def _menuloop(self):
        print(f"Office Solutions Corporation\nSales Reporting Application "
              "v{APP_VERSION}")
        print("===============================================")
        print("[1] Login with E-Mail address")
        print("[2] Register a New User")
        print("===============================================")
        menu_selection = input("Please enter an option [1-2, q to Quit] : ")
        if menu_selection == "1":
            if self.mylogin.login() is True:
                return menu_module.Menu(self.mydb).createMenu()
        elif menu_selection == "2":
            Add_User.UserController(self.mydb).addNewUser()
        elif menu_selection == "q" or menu_selection == "Q":
            print("\nGoodbye!")
            return False
        elif menu_selection == "":
            print("\nNot a valid choice. Please try again.")
        else:
            print("\nNot a valid choice. Please try again.")
        return True


if __name__ == "__main__":
    m = Main()
    m.run()
