import fileinput, runpy, Mainframe

user = input("Username: ")
passw = input("Password: ")

if user == "admin":
    if passw == "adminpassword":
        f = open("Users.txt", "a")
        newu = input("""
Enter new user: """)
        newp = input("""
Enter password: """)
        if newp == input("Confirm password: "):
            print("""
User added successfully!
""")
            f.write(str(";"+newu))
            f.close()
            Mainframe.Main()
        else:
            print("Passwords not same!")
            Mainframe.Main()
    else:
        print("""You do not have the authorisation
to execute this operation.
""")
        Mainframe.Main()
else:
    print("""You do not have the authorisation
to execute this operation.
""")
    Mainframe.Main()
