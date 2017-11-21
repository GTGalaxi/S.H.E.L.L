import math, runpy
tri = int(input("""
Number of lines: """))
for i in range(1, tri+1):
    print(("* "*i).rstrip())
runpy.run_path("Shapes.py")
