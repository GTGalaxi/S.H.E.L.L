import math, runpy
Term = int(input("n: "))
n1 = int(0)
n2 = int(1)
nf = int(0)
print(n1)
print(n2)
for i in range(Term-2):
    nf = n1+n2
    print(nf)
    n1 = n2
    n2 = nf
runpy.run_path("MathSub.py")
