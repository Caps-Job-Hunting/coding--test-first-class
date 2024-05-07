import copy

N, M = map(int, input().split())
office_map = []
cctv_list_idx = []
cctv_list = []
all_cases = []

# 왼, 아, 오 , 위
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

direction = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[2, 3], [1, 2], [0, 1], [0, 3]],
    4: [[0, 2, 3], [1, 2, 3], [0, 1, 2], [0, 1, 3]],
    5: [[0, 1, 2, 3]]
}

for _ in range(N):
    office_map.append(list(map(int, input().split())))

for j in range(N):
    for i in range(M):
        if office_map[j][i] != 0 and office_map[j][i] != 6:
            cctv_list_idx.append([j, i])
            cctv_list.append(office_map[j][i])


def caseList(idx, path):
    # 모든 CCTV를 확인했을 경우, 경로를 결과에 추가하고 반환
    if idx == len(cctv_list):
        all_cases.append(path)
        return

    cctv_num = cctv_list[idx]  # 현재 CCTV 번호
    for dirs in direction[cctv_num]:  # 현재 CCTV의 가능한 모든 방향에 대해
        # 다음 CCTV로 넘어가면서 현재 CCTV의 방향 조합을 경로에 추가
        caseList(idx + 1, path + [dirs])


caseList(0, [])
result = int(1e9)

for case in all_cases:
    copy_office = copy.deepcopy(office_map)
    result_now = 0
    for j in range(len(case)):
        for i in range(len(case[j])):
            ny = cctv_list_idx[j][0]
            nx = cctv_list_idx[j][1]
            while True:
                ny += dy[case[j][i]]
                nx += dx[case[j][i]]
                if not (0 <= ny < N and 0 <= nx < M) or copy_office[ny][nx] == 6:
                    break
                if copy_office[ny][nx] == 0:
                    copy_office[ny][nx] = '#'
    for row in copy_office:
        result_now += row.count(0)

    result = min(result, result_now)

print(result)
