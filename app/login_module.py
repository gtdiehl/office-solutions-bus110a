class Login:
    
    def __init__(self, mydb):
        '''
        The function above allows for connection to the database
        '''
        self.mydb = mydb
        
    def login(self):
        login_successful = False
        '''
        The for loop starts at a range of 3 to 1. -1 subtracts from 3 for
        each unsuccessful attempt
        '''
        for i in range(3, 0, -1):

            email = input("Please enter email: ")
            password = input("Please enter password: ")

            results = self.mydb.query_user_db("SELECT EXISTS(SELECT * FROM "
                                              "Employee WHERE Email is ? AND "
                                              "Password is ?)", 
                                              (email, password))

            if results == [1]:
                print("\nLogin Successful")
                login_successful = True
                break
            else:
                if i > 1:
                    print("Unsuccessful login attempt.  Please try again. "
                          "Note that e-mail addresses and passwords are "
                          "case-sensitive.")
                else:
                    print("Unsuccessful login attempt. Note that e-mail "
                          "addresses and passwords are case-sensitive.")
                
        if login_successful:
            return True
        else:
            print("Please contact your administrator for your login "
                  "credentials.")
            return False
