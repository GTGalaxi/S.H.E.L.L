import fileinput, runpy, getpassmod, LogonStuff, UserPassPull

user = input("Username: ")
password = getpassmod.getpass("Password: ")

UserPassPull.Logon(user, password)
