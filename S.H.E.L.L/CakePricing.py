import math
import winsound
import fileinput
import runpy

side1 = float(input('Cake 1 side length (cm): '))
cost1 = float(input('Cake 1 cost ($) '))
side2 = float(input('Cake 2 side length (cm): '))
cost2 = float(input('Cake 2 cost ($) '))

cake1_area = side1**2
cake1_costpcm2 = cost1/cake1_area
cake2_area = side2**2
cake2_costpcm2 = cost2/cake2_area

print('Cake 1 costs ${:.2f} per cm2 for {:.0f} cm2'.format(cake1_costpcm2, cake1_area))
print('Cake 2 costs ${:.2f} per cm2 for {:.0f} cm2'.format(cake2_costpcm2, cake2_area))

if cake1_costpcm2 == cake2_costpcm2:
  print('Get either!')
elif cake1_costpcm2 < cake2_costpcm2:
  print('Get cake 1!')
elif cake1_costpcm2 > cake2_costpcm2:
  print('Get cake 2!')

runpy.run_path("CakeSub.py")

