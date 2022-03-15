f = open('input.txt', 'r')

map = []

line = f.readline()
while line:
    map.append(line.strip.split(''))
    line = f.readline()

print(map)
f.close()