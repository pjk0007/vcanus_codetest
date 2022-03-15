f = open('input.txt', 'r')
land = []

line = f.readline()
while line:
    land.append(line.strip().split(' '))
    line = f.readline()

f.close()

rc = [(0,-1), (-1,0), (0,1), (1,0)]

def BFS(i, j):
    queue = []
    queue.append((i,j, 0))
    while True:
        row, col, cnt = queue.pop(0)
        if(land[row][col] == '0'):break
        else:
            for r,c in rc:
                queue.append((row+r, col+c, cnt+1))
    land[i][j] = cnt


for i in range(0, len(land)):
    for j in range(0, len(land[i])):
        if(land[i][j]=='0') : continue
        BFS(i,j)

for i in range(0, len(land)):
    for j in range(0, len(land[i])):
        print(land[i][j], end='')
    print()

