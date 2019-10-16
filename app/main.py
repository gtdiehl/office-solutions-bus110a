import database
import loginfunction


def main():
    mydb = database.Database()
    mylogin = loginfunction.login(mydb)

    mylogin.login()

if __name__ == "__main__":
    main()