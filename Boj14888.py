import sys

N = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_v = -1e9
min_v = 1e9

def dfs(num, cnt, add, sub, mul, div):
    global max_v, min_v
    
    if cnt == N:
        max_v = max(max_v, num)
        min_v = min(min_v, num)
        return
    else:
        if add > 0:
            dfs(num + A[cnt], cnt + 1, add - 1, sub, mul, div)
        if sub > 0:
            dfs(num - A[cnt], cnt + 1, add, sub - 1, mul, div)
        if mul > 0:
            dfs(num * A[cnt], cnt + 1, add, sub, mul - 1, div)
        if div > 0:
            dfs(int(num / A[cnt]), cnt + 1, add -1, sub, mul, div - 1)
            
dfs(A[0], 1, add, sub, mul, div)

print(max_v)
print(min_v)