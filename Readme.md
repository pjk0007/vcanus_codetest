# 5번 설명

*input.txt*에 있는 인풋값 읽어와서 *land*라는 2차원 배열에 저장
```python
f = open('input.txt', 'r')
land = []

line = f.readline()
while line:
    land.append(line.strip().split(' '))
    line = f.readline()

f.close()
```

각 셀에서 왼쪽, 위, 오른쪽, 아래로 이동하기 위해 배열 정의

```python
rc = [(0,-1), (-1,0), (0,1), (1,0)]

```


i, j에 해당하는 셀에서 시작하여 가장 가까운 *0*이 있는 위치까지 거리(*cnt*) 구하기
큐에 현재 위치 및 이동한 거리 저장 후 *0*이 아니면 주변 셀의 위치와 *cnt+1*을 큐에 저장
*0*을 만나면 그 위치를 *cnt*로 변경
```python
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
```

*land*에 존재하는 모든 셀을 이동하며 *0*인 경우는 *continue*
*0*이 아닌경우 *BFS*실행하여 해당 셀의 값 변경
```python
for i in range(0, len(land)):
    for j in range(0, len(land[i])):
        if(land[i][j]=='0') : continue
        BFS(i,j)
```

결과값 출력
```python
for i in range(0, len(land)):
    for j in range(0, len(land[i])):
        print(land[i][j], end=' ')
    print()
```

## 결과값
```
0 0 0 0 0 0 0 0 0 0 
0 0 0 0 1 0 0 0 0 0 
0 0 0 1 2 1 0 0 0 0 
0 1 1 2 3 2 1 0 0 0 
0 1 2 3 4 3 2 1 1 0 
0 1 2 3 4 3 3 2 1 0 
0 0 1 2 3 2 2 1 0 0 
0 0 0 1 2 1 1 0 0 0 
0 0 0 0 1 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 0 
```



