f = open('input.txt', 'r')

map = []

line = f.readline()
while line:
    map.append(line.strip().split(' '))
    line = f.readline()

for col in map:
    for row in col:
        print("col", end='')
    print() 
f.close()