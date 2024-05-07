N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0

for i in A:
    left = i - B
    result += 1
    if left >= 0:
        if left % C == 0:
            result += left // C
        else:
            result += left // C + 1

print(result)
