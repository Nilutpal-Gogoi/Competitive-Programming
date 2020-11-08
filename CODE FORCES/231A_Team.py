# https://codeforces.com/problemset/problem/231/A


n = int(input())
result = 0
for _ in range(n):
    count = 0
    lis = list(map(int, input().split(" ")))
    for i in lis:
        if i == 1:
            count += 1
    if count > 1:
        result += 1
print(result)