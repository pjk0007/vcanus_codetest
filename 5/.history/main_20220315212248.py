f = open('input.txt', 'r')

map = []

line = None
while line !='':
    line = f.readline()
    map.append(line.split(' '))

print(map)
f.close()