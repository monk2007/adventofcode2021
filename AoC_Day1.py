with open('puzzleinput/puzzle1.txt') as f:
    readingsAsStrings = f.readlines()
readings = list(map(int, readingsAsStrings))

# Part 1
increases = 0
for i in range(len(readings) - 1):
  increases += 1 if readings[i+1] > readings[i] else 0

print('Day 1 - Part 1 - There were ' + str(increases) + ' increases')

# Part 2
increases = 0
for i in range(len(readings) - 3):
    increases += 1 if sum(readings[i+1 : i+4]) > sum(readings[i : i+3]) else 0

print('Day 1 - Part 2 - There were ' + str(increases) + ' increases')