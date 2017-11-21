import math, Mainframe
a = int(input("""
Divisions: """))
div = []
beat = []
for i in range(a):
    div.append(int(input("Divisible by: ")))
b = int(input("Number of beats to print: "))
for o in range(b):
    e = o+1
    for p in range(a):
        c = (e)%div[p]
        if c == 0:
            beat.append("X")
        else:
            beat.append(" ")
    beat2 = "".join(beat)
    beat3 = str(beat2).rstrip()
    if b < 10:
        d = str(e)
    elif b < 100:
        if e < 10:
            d = " "+str(e)
        else:
            d = str(e)
    else:
        if e < 10:
            d = "  "+str(e)
        elif e < 100:
            d = " "+str(e)
        else:
            d = str(e)
    print(d+":"+beat3)
    beat = []
Mainframe.Start()
