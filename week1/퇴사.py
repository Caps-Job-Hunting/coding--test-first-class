def calDay(n, t, p):
    # n+1일을 포함하기 위해 n+1 크기로 dp 배열 초기화
    dp = [0] * (n + 2)

    for i in range(1, n + 1):
        # 오늘 상담을 하지 않을 때 최대 수익
        dp[i] = max(dp[i], dp[i - 1])
        # 오늘 상담을 할 때
        next_day = i + t[i - 1]  # 상담이 끝나는 다음 날
        if next_day <= n + 1:  # 퇴사일을 넘지 않으면 상담을 진행
            dp[next_day] = max(dp[next_day], dp[i] + p[i - 1])

    # 퇴사일에 가능한 최대 수익 출력
    return max(dp)


# 입력 받기
n = int(input())
t = []
p = []
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

# 함수 호출 및 결과 출력
print(calDay(n, t, p))
