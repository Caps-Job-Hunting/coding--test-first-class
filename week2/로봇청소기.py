n, m = map(int, input().split())
x, y, side = map(int, input().split())
robotPosition = [x, y]
cleanMap = []

# 방향 변환을 위한 dx, dy 정의 (북, 동, 남, 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# MAP 생성
for i in range(n):
    cleanMap.append(list(map(int, input().split())))


def turnLeft():
    global side
    side = (side - 1) % 4  # 왼쪽으로 회전


def clean():
    global robotPosition, side
    count = 0  # 청소하는 칸의 수
    turn_time = 0  # 회전한 횟수

    while True:
        # 현재 위치 청소
        if cleanMap[robotPosition[0]][robotPosition[1]] == 0:
            cleanMap[robotPosition[0]][robotPosition[1]] = 2  # 청소한 곳을 2로 표시
            count += 1

        # 왼쪽 방향으로 회전한 후, 그 방향에 청소할 공간이 있는지 확인
        turnLeft()
        nx = robotPosition[0] + dx[side]
        ny = robotPosition[1] + dy[side]

        if cleanMap[nx][ny] == 0:  # 청소할 공간이 있다면 이동
            robotPosition[0] = nx
            robotPosition[1] = ny
            turn_time = 0
            continue
        else:
            turn_time += 1

        # 네 방향 모두 청소할 곳이 없거나 벽인 경우
        if turn_time == 4:
            nx = robotPosition[0] - dx[side]
            ny = robotPosition[1] - dy[side]
            # 뒤로 이동할 수 있는 경우
            if cleanMap[nx][ny] != 1:
                robotPosition[0] = nx
                robotPosition[1] = ny
            else:  # 뒤가 벽이라 이동할 수 없는 경우
                break
            turn_time = 0

    return count


# 청소 시작
result = clean()
print(result)
