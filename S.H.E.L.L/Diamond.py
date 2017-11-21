import math, runpy
width = int(input('''
Enter width: '''))
for i in range(1, width + 1):
    print(' ' * (width - i) + ' '.join(['*'] * i))
for i in range(width - 1, 0, -1):
    print(' ' * (width - i) + ' '.join(['*'] * i))
runpy.run_path("Shapes.py")
