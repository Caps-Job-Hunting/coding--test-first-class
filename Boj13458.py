N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = N     # 시험장 당 주감독관 한명 꼭 필요

for i in A:
    i -= B      # 주감독관이 관리 
    if i > 0:   # 못하는 애들 있으면
        if (i % C) != 0:
            cnt += ( i // C ) + 1
        else: 
            cnt += (i // C) 

print(cnt)