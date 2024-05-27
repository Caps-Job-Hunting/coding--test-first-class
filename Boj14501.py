N = int(input())

schedule = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(N-1, -1, -1):
    if i + schedule[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i + schedule[i][0]] + schedule[i][1])
print(dp[0])
        
    
# 이해가 안돼.......... 될 듯 말듯.. max 구하는 부분 생각해보기
