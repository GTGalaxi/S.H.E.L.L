import fileinput, getpass, LogonStuff

Passwords = []
Users = []

def Logon(username, password):
    for passw in fileinput.input("Passwords.txt"):
        Passwords = passw.split(";")
    for user in fileinput.input("Users.txt"):
        Users = user.split(";")
    for index in range(len(Users)):
        userX = Users[index].replace("'","")
        passX = Passwords[index].replace("'","")
        if username == userX:
            if password == passX:
                LogonStuff.Success(username)
    LogonStuff.Fail()

    
