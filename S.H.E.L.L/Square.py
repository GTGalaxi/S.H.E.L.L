import math, runpy
a = int(input("""
Enter the length of the side: """))
b = "* "*a
print(b.rstrip())
for i in range(a-2):
  print("*","  "*(a-2)+"*")
print(b.rstrip())
runpy.run_path("Shapes.py")
