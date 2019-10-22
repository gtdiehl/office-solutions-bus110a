import database
import loginfunction
import menu_module


def main():
    mydb = database.Database()
    mylogin = loginfunction.login(mydb)

    if mylogin.login() is True:
        menu_module.BestMenu(mydb).createBestMenu()

if __name__ == "__main__":
    main()
