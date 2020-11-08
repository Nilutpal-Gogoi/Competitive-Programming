# https://codeforces.com/problemset/problem/339/A


t = input()
lis = list(t)
for i in range(0, len(lis)-2, 2):
    for j in range(i+2, len(lis), 2):
        if lis[i]>lis[j]:
            lis[i], lis[j] = lis[j], lis[i]
t = "".join(lis)
print(t)