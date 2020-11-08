# https://codeforces.com/contest/1391/problem/B


# Not an efficient solution
#
# t = int(input())
# for _ in range(t):
#     n,m = map(int, input().split())
#     lis = []
#     for i in range(n):
#         temp = []
#         for j in range(m):
#             temp.append(str(input()))
#         lis.append(temp)
#     count = 0
#     for i in range(n-1):
#         if lis[i][n-1] == "R":
#             count += 1
#     for i in range(m-1):
#         if lis[n-1][i] == "D":
#             count += 1
#     print(count)

# Efficient One

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    count = 0
    for i in range(n-1):
        x = input()
        if x[-1] == "R":
            count += 1
    x = input()
    for j in range(m-1):
        if x[j] == "D":
            count += 1
    print(count)