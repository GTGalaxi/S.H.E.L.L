import math, runpy
num = int(input("""
Enter a number: """))
for i in range(1 , num+1):
    print(i, "squared is", i*i)
runpy.run_path("MathSub.py")      
