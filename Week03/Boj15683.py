import copy

# NxM 사무실 
n, m = map (int, input().split())
#cctv 종류, x 좌표, y좌표 저장 배열 
cctv = []
#cctv 방향 정보 
mode = [
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[3,0]],
    [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    [[0,1,2,3]]
]
#사무실 정보 
board = []

#위 좌 아래 왼 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#사무실 안에 cctv 와 벽 정보 저장 

for i in range(n):
    data = list(map(int, input().split()))
    board.append(data)
    for j in range(m):
        if data[j] in [1,2,3,4,5]:
            #cctv의 정보를 저장 (cctv mode, x, y 좌표)
            cctv.append([data[j],i,j])

#cctv로 감시 가능한 부분 채우는 함수 
def fill(board, mode, x, y):
    for i in mode: 
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            #범위 넘으면 중단 
            if nx <0 or nx >= n or ny <0 or ny >= m:
                break
            #벽에 닿으면 중단 
            if board[nx][ny] == 6:
                break
            #감시가능 (-1이 감시 가능하다는 뜻)
            elif board[nx][ny] == 0:
                board[nx][ny] = -1 

# 백트래킹 -> DFS방법에서 불필요한 부분 제거하는 방법! 
# 모드에 따라 사각지대의 개수가 달라짐 -> 깊이 우선 탐색으로 최소값 찾기 
def dfs(depth, board):
    global min_value
    # 탐색 완료 조건 
    if depth == len(cctv):
        count = 0 
        for i in range(n):
            #board의 각 행에서 0 개수 찾기 
            count += board[i].count(0)
            #최소값 업데이트 
        min_value = min(min_value,count)
        return
    
    temp = copy.deepcopy(board)
    cctv_num, x, y = cctv[depth] #탐색할 cctv 설정 
    for i in mode[cctv_num]:
        fill(temp, i , x, y) 
        dfs(depth+1, temp)
        temp = copy.deepcopy(board)

min_value = 100000
dfs(0, board)
print(min_value)
    
    
    