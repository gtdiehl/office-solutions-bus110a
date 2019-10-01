class Login:
    def __init__(self, myDB):
        self.myDB = myDB
    
    def startLogin(self):
        loginRetries = 0
        while(loginRetries < 3):
            username = input("Enter in Username: ")
            password = input("Enter in Password: ")
            
            results = self.myDB.queryDB("SELECT EXISTS(SELECT * FROM Employee WHERE Email is \'" +
                                       username + "\' AND Password is \'" + 
                                       password + "\')")

            if(results[0] == 1):
                print("Login Successful")
                return True
            else:
                print("Incorrect user credentials")
                loginRetries += 1
                
        return False
            