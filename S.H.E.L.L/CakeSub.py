import math, runpy, Mainframe
print("""
Welcome to the cake store

Avaliable cake related programs:
 * Cakeulator
 * Cake Pricing
 * Exit
 """)
a = input("Which cake program do do you need? ")
b = a.lower()
c = b.replace(" ","")
if c == "cakeulator":
      print("")
      runpy.run_path("Cakeulator.py")
elif c == "cakepricing":
      print("")
      runpy.run_path("CakePricing.py")
elif c == "exit":
      Mainframe.Start()
else:
      print("Sorry, but this program does not exist.")
      runpy.run_path("CakeSub.py")

