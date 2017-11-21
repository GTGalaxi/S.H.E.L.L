import math, Mainframe
nrows = int(input('''
Number of lines: '''))
state = input('Start line: ')

length = len(state)
for i in range(nrows):
  print(state)
  line = ''
  for i in range(length):
    if state[i - 1] != state[(i + 1) % length]:
      line += '*'
    else:
      line += '.'
  state = line
Mainframe.Start()
