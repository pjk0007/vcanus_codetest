
### 데이터 읽어오기
f = open('./input.txt', 'r')
land = []

line = f.readline()
while line:
    land.append(line.strip().split(' '))
    line = f.readline()

f.close()
###

rc = [(0,-1), (-1,0), (0,1), (1,0)] # 좌, 싱, 우, 하

### 하나의 셀에서 가장 가까운 0 찾기 (최단거리)
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

### 모든 셀을 돌아가며 BFS 실행
for i in range(0, len(land)):
    for j in range(0, len(land[i])):
        if(land[i][j]=='0') : continue
        BFS(i,j)


### 결과 출력
for i in range(0, len(land)):
    for j in range(0, len(land[i])):
        print(land[i][j], end=' ')
    print()

