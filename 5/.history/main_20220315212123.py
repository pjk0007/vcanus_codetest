f = open('input.txt', 'r', encoding='utf-8')

map = []

line = ''
while line !='':
    line = f.readline()
    print(line)

f.close()