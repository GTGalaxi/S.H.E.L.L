import math
import winsound
import fileinput
import runpy
for txt in fileinput.input("Users.txt"):
    users = (txt)
user = input("Username: ")
password = input("Password: ")
f = open("Users.txt", "a")
if user == "admin" and password == "adminpassword":
    remu = input("""
Enter user to delete: """)
    if remu in users:
        print("""
Are you sure you wish to remove this user -""",remu+"?")
        sure = input("(Y/N) ")
        remu = remu+","
        if sure == "y":
            f.replace(remu,"")
            print("""User removed successfully!
""")
            f.close()
        else:
            print("""User delete cancelled.
""")
    else:
        print("""User does not exist.
""")
else:
    print("You do not have sufficient administrator rights.")
runpy.run_path("Mainframe.py")
                 
