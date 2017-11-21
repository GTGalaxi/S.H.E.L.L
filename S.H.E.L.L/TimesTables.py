import math, runpy
num = int(input("""
What number do you want to see
the times tables for? """))
for i in range(1,12):
    print(i,"x",num,"=",num*i)
runpy.run_path("MathSub.py")
