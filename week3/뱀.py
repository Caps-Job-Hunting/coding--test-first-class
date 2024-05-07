from collections import deque

# 아래, 왼, 위, 오르쪽
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]
nx = 0
ny = 0

N = int(input())
K = int(input())
apple_position = []

for _ in range(K):
    row, col = map(int, input().split())
    apple_position.append([row - 1, col - 1])

L = int(input())
move_snake = {}
for _ in range(L):
    X, C = map(str, input().split())
    move_snake[int(X)] = C


def turnSnake(direction, turn_side):
    global ny
    global nx
    global idx

    if turn_side == 'L':
        idx = (idx + 7) % 4
    elif turn_side == 'D':
        idx = (idx + 5) % 4

    if direction[idx] == 'D':
        ny += dy[0]
        nx += dx[0]
    elif direction[idx] == 'L':
        ny += dy[1]
        nx += dx[1]
    elif direction[idx] == 'U':
        ny += dy[2]
        nx += dx[2]
    elif direction[idx] == 'R':
        ny += dy[3]
        nx += dx[3]


q = deque()
q.appendleft([0, 0])
snake_dir = ['U', 'R', 'D', 'L']
idx = 1
count = 0
while True:
    if count in move_snake:
        turn = move_snake[count]
    else:
        turn = 'P'
    turnSnake(snake_dir, turn)
    if 0 <= ny < N and 0 <= nx < N:
        q.appendleft([ny, nx])
        if any(same == q[0] for same in list(q)[1:]):
            count += 1
            break
        if q[0] in apple_position:
            apple_position.remove(q[0])
        else:
            q.pop()
    else:
        count += 1
        break
    count += 1

print(count)
