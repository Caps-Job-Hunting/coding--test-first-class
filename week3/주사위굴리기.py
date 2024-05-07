N, M, dice_y, dice_x, K = map(int, input().split())
dice_map = []
for _ in range(N):
    dice_map.append(list(map(int, input().split())))

move_list = list(map(int, input().split()))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
dice = [0, 0, 0, 0, 0, 0]


def turnDice(turn):
    if turn == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif turn == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif turn == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif turn == 4:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]


for i in move_list:
    if 0 <= dice_y + dy[i - 1] < N and 0 <= dice_x + dx[i - 1] < M:
        turnDice(i)
        dice_x += dx[i - 1]
        dice_y += dy[i - 1]
        if dice_map[dice_y][dice_x] == 0:
            dice_map[dice_y][dice_x] = dice[5]
        else:
            dice[5] = dice_map[dice_y][dice_x]
            dice_map[dice_y][dice_x] = 0
        print(dice[0])
