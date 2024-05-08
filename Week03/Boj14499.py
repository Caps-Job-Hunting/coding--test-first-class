
# 주사위를 굴렸을 때의 변하는 index 계산 
def roll(move):
    #동쪽으로 굴릴경우
    if move == 1:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]
    #서쪽으로 굴릴경우 
    if move == 2:   
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]
    #북쪽으로 굴릴경우 
    if move == 3:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]
    #남쪽으로 굴릴경우 
    if move == 4:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]
    
import sys
N, M, y, x, K = map (int, sys.stdin.readline().split())
board = [list(map (int, sys.stdin.readline().split())) for _ in range(N)]
K_order = list(map (int, sys.stdin.readline().split()))
# 맨 처음 주사위의 모든 면은 0이다. 
dice =[0,0,0,0,0,0]

#x값은 서쪽에서 떨어진 카의 개수 
dy = [0,0,-1,1]
#y값은 북쪽으로 떨어진 칸의 개수 
dx = [1,-1,0,0]

for i in K_order:
    if (0 <= y + dy[i-1] < N and  0 <= x + dx[i-1] < M) :
        x = x + dx[i-1] 
        y = y + dy[i-1]
        
        roll(i)
        if board[y][x] == 0:
            board[y][x] = dice[5]
        else:
            dice[5] = board[y][x]
            board[y][x] = 0
        
        print(dice[0])