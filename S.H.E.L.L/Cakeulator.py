import math
import winsound
import fileinput
import runpy
a = int(input("Guests: "))
b = int(input("Cakes: "))
c = int(input("Pieces: "))
d = b*c
if d == a:
    print("No leftovers :(")
elif d > a:
    print("Leftovers:", d-a)
elif d < a:
    print("Quick! Go buy more cake!")
runpy.run_path("CakeSub.py")
