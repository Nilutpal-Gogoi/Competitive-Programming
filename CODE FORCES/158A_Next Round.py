# https://codeforces.com/problemset/problem/158/A


n, k = map(int, input().split())
count = 0
lis = list(map(int, input().split()))
for i in range(len(lis)):
    if lis[i] > 0:                       # Given in question that the score should be positive
        if lis[i] >= lis[k-1]:
            count += 1
        else:
            break
print(count)
