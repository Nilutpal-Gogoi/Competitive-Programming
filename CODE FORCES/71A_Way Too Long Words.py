# https://codeforces.com/problemset/problem/71/A


n = int(input())
for _ in range(n):
    string = str(input())
    if len(string) > 10:
        print(string[0]+str((len(string)-2))+string[-1])
    else:
        print(string)