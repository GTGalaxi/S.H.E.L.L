import math
import winsound
import fileinput
import runpy
number1 = int(input("""
Enter First Number: """))
number2 = int(input("Enter Second Number: "))
decider2 = str(input("Do you want to x, /, + or - ? "))
decider = decider2.lower()
if decider == str("x"):
    print("""
The answer is:""",number1*number2)
    print(" ")
elif decider == str("/"):
    print("""
The answer is:""",number1/number2)
    print(" ")
elif decider == str("+"):
    print("""
The answer is:""",number1+number2)
    print(" ")
elif decider == str("-"):
    print("""
The answer is:""",number1-number2)
    print(" ")
runpy.run_path("MathSub.py")      
