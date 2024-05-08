
from collections import deque

#보드의 크기 
N = int(input())
#사과의 개수 
K = int(input())

#그래프(map) 만들기 NxN 초기의 값을 다 0으로 설정 
graph = [[0] * N for _ in range(N)]

#사과가 있는 위치를 2로 설정 
for i in range(K):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 2

#뱀의 방향 변환 횟수 L 
L = int(input())  

#뱀의 방향 변환 정보 저장 딕셔너리 
L_dict = dict()
#최초 방향은 오른쪽! index는 0!
direction = 0
#방향 별 x,y 값의 변화값 저장 
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(L):
    x,c = input().split()
    L_dict[int(x)] = c

#뱀의 첫 위치 저장 
x, y = 0, 0
graph[x][y] = 1

#방향 전환 함수 
#오른쪽으로 틀수록 index가 올라감 
def turn_dir(c):
    global direction 
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

#시간 초기화 
cnt = 0
#꼬리의 정보 저장할 큐 초기화 
queue = deque()
#2차원 배열이므로 튜플 형식으로 정보 저장 
queue.append((0,0))


#움직이기 시작 
while True:
    cnt += 1
    x += dx[direction]
    y += dy[direction]
    
    #주어진 graph 각 벽에 닿으면 게임 종료 
    if x < 0 or x >= N or y <0 or y >= N :
        break

    #사과를 만났을 경우 
    if graph[x][y] == 2:
        graph[x][y] = 1
        #꼬리가 사라지지 않으므로 큐에 저장! 
        queue.append((x,y))
        #해당 초의 방향 전환 정보가 있을시 
        if cnt in L_dict:
            turn_dir(L_dict[cnt])
    
    #사과를 안만났을 경우 
    elif graph[x][y] == 0:
        graph[x][y] = 1
        queue.append((x,y))
        
        #꼬리의 정보를 없애야 함!
        tx, ty = queue.popleft()
        graph[tx][ty] = 0 #2에서 0으로 업데이트
        
        #해당 초의 방향 전환 정보가 있을시 
        if cnt in L_dict:
            turn_dir(L_dict[cnt])
    
    else: 
        break

print(cnt)