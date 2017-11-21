import runpy

print("""
Welcome to the shapes program!

Please choose one of the following shapes:
 * Diamond
 * Square
 * Triangle
 * Exit
""")
program = input("Shape: ")
program2 = program.lower()
program3 = program2.replace(" ","")
if program3 == str("diamond"):
    runpy.run_path("Diamond.py")
elif program3 == str("square"):
    runpy.run_path("Square.py")
elif program3 == str("triangle"):
    runpy.run_path("Triangle.py")
elif program3 == ("exit"):
    runpy.run_path("Mainframe.py")
else:
    print("""That shape is not avaliable,
Try another shape""")
    runpy.run_path("Shapes.py")
