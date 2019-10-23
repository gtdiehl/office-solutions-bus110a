import Add_User
import database
import loginfunction
import menu_module

mydb = database.Database()
mylogin = loginfunction.login(mydb)


def main():
    ans = True
    while ans:
        ans = _menuloop()


def _menuloop():
    print("Office Solutions Corporation\nSales Reporting Application v1.0")
    print("===============================================")
    print("[1] Login with E-Mail address")
    print("[2] Register a New User")
    print("===============================================")
    menu_selection = input("Please enter an option [1-2, q to Quit] : ")
    if menu_selection == "1":
        if mylogin.login() is True:
            return menu_module.BestMenu(mydb).createBestMenu()
    elif menu_selection == "2":
        Add_User.UserController(mydb).addNewUser()
    elif menu_selection == "q" or menu_selection == "Q":
        print("\nGoodbye!")
        return False
    elif menu_selection == "":
        print("\nNot a valid choice. Please try again.")
    else:
        print("\nNot a valid choice. Please try again.")
    return True


if __name__ == "__main__":
    main()
