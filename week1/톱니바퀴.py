shouldTurnGearList = []
shouldTurnGearSide = []
gear_list = [[0]]
for _ in range(4):
    gear_list.append(list(map(int, input().rstrip())))

K = int(input())
turn_case = []

for _ in range(K):
    turn_case.append(list(map(int, input().split())))


# 시계방향
def turnGearRight(gear):
    a = 7
    temp = gear[7]
    for _ in range(len(gear) - 1):
        gear[a] = gear[a - 1]
        a -= 1
    gear[a] = temp
    return gear


# 반시계방향
def turnGearLeft(gear):
    a = 0
    temp = gear[0]
    for _ in range(len(gear) - 1):
        gear[a] = gear[a + 1]
        a += 1
    gear[7] = temp
    return gear


for gear_num, turn_dir in turn_case:
    direction = turn_dir
    shouldTurnGearList.clear()
    shouldTurnGearSide.clear()
    if gear_num == 1:
        shouldTurnGearList.append(gear_num)
        shouldTurnGearSide.append(direction)
        for i in range(1, 4):
            if gear_list[i][2] != gear_list[i + 1][6]:
                shouldTurnGearList.append(i + 1)
                if direction == 1:
                    direction = -1
                    shouldTurnGearSide.append(direction)
                else:
                    direction = 1
                    shouldTurnGearSide.append(direction)
            else:
                break
    elif gear_num == 2:
        shouldTurnGearList.append(gear_num)
        shouldTurnGearSide.append(direction)
        if gear_list[gear_num][6] != gear_list[gear_num - 1][2]:
            shouldTurnGearList.append(gear_num - 1)
            if direction == 1:
                direction = -1
                shouldTurnGearSide.append(direction)
            else:
                direction = 1
                shouldTurnGearSide.append(direction)
        for i in range(0, 2):
            if gear_list[gear_num + i][2] != gear_list[gear_num + i + 1][6]:
                shouldTurnGearList.append(gear_num + i + 1)
                if i == 0:
                    if turn_dir == direction:
                        if direction == 1:
                            direction = -1
                            shouldTurnGearSide.append(direction)
                        else:
                            direction = 1
                            shouldTurnGearSide.append(direction)
                    else:
                        direction = turn_dir
                        if direction == 1:
                            direction = -1
                            shouldTurnGearSide.append(direction)
                        else:
                            direction = 1
                            shouldTurnGearSide.append(direction)
                else:
                    if direction == 1:
                        direction = -1
                        shouldTurnGearSide.append(direction)
                    else:
                        direction = 1
                        shouldTurnGearSide.append(direction)
            else:
                break

    elif gear_num == 3:
        shouldTurnGearList.append(gear_num)
        shouldTurnGearSide.append(direction)
        if gear_list[gear_num][2] != gear_list[gear_num + 1][6]:
            shouldTurnGearList.append(gear_num + 1)
            if direction == 1:
                direction = -1
                shouldTurnGearSide.append(direction)
            else:
                direction = 1
                shouldTurnGearSide.append(direction)
        for i in range(0, 2):
            if gear_list[gear_num - i][6] != gear_list[gear_num - i - 1][2]:
                shouldTurnGearList.append(gear_num - i - 1)
                if i == 0:
                    if turn_dir == direction:
                        if direction == 1:
                            direction = -1
                            shouldTurnGearSide.append(direction)
                        else:
                            direction = 1
                            shouldTurnGearSide.append(direction)
                    else:
                        direction = turn_dir
                        if direction == 1:
                            direction = -1
                            shouldTurnGearSide.append(direction)
                        else:
                            direction = 1
                            shouldTurnGearSide.append(direction)
                else:
                    if direction == 1:
                        direction = -1
                        shouldTurnGearSide.append(direction)
                    else:
                        direction = 1
                        shouldTurnGearSide.append(direction)
            else:
                break
    elif gear_num == 4:
        shouldTurnGearList.append(gear_num)
        shouldTurnGearSide.append(direction)
        for i in range(4, 1, -1):
            if gear_list[i][6] != gear_list[i - 1][2]:
                shouldTurnGearList.append(i - 1)
                if direction == 1:
                    direction = -1
                    shouldTurnGearSide.append(direction)
                else:
                    direction = 1
                    shouldTurnGearSide.append(direction)
            else:
                break

    # 실제 톱니바퀴 회전
    for k in range(len(shouldTurnGearList)):
        turn_gear = gear_list[shouldTurnGearList[k]][:]
        if shouldTurnGearSide[k] == -1:
            gear_list[shouldTurnGearList[k]][:] = turnGearLeft(turn_gear)
        else:
            gear_list[shouldTurnGearList[k]][:] = turnGearRight(turn_gear)

answer = 0
count = 1
for j in range(1, 5):
    if gear_list[j][0] == 1:
        answer += count
    count *= 2

print(answer)
