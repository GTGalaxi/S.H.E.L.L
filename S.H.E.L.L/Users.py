import fileinput, runpy, Mainframe
userlist = """
Available Users:
"""
print(userlist)
for txt in fileinput.input("Users.txt"):
    txt = txt.replace(";","""
""")
    print(txt, end="")
print()
Mainframe.Main()
