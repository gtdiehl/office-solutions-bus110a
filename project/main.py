import login_module
import menu_module
import db_module

def main():
    myDB = db_module.Database()
    login = login_module.Login(myDB)
    
    if(login.startLogin()):
        menu_module.Menu(myDB).createMenu()

if __name__ == "__main__":
    main()