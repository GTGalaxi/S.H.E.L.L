import math
import winsound
import fileinput
import runpy
TOP = 1
MIDDLE = 2
BOTTOM = 3

LEFT = 4
RIGHT = 5

HORIZONTAL = {
    TOP: set("02356789"),
    MIDDLE: set("2345689"),
    BOTTOM: set("0235689"),
}

VERTICAL = {
    TOP: {
      LEFT: set("045689"),
      RIGHT: set("01234789"),
    },
    BOTTOM: {
      LEFT: set("0268"),
      RIGHT: set("013456789"),
    },
}

def print_horizontal(num, state, width, end):
  out = " " * (width + 2)
  if num in HORIZONTAL[state]:
    out = " " + "-" * width + " "
  print(out, end=end)

def print_vertical(num, state, width, end):
  out = " "
  if num in VERTICAL[state][LEFT]:
    out = "|"
  out += " " * (width)
  if num in VERTICAL[state][RIGHT]:
    out += "|"
  else:
    out += " "
  print(out, end=end)

def get_end(i, length):
  if i == length - 1:
    return "\n"
  return " "

def calculator_print(num, width):
  num = str(num)
  for i, c in enumerate(num):
    print_horizontal(c, TOP, width, get_end(i, len(num)))
  for _ in range(width):
    for i, c in enumerate(num):
      print_vertical(c, TOP, width, get_end(i, len(num)))
  for i, c in enumerate(num):
    print_horizontal(c, MIDDLE, width, get_end(i, len(num)))
  for _ in range(width):
    for i, c in enumerate(num):
      print_vertical(c, BOTTOM, width, get_end(i, len(num)))
  for i, c in enumerate(num):
    print_horizontal(c, BOTTOM, width, get_end(i, len(num)))

print("")
num = int(input("Number: "))
width = int(input("Width: "))
calculator_print(num, width)
runpy.run_path("MathSub.py")
