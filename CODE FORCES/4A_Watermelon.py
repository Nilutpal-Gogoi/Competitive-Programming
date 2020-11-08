# https://codeforces.com/problemset/problem/4/A


w = int(input())
if w % 2 == 0:
    if w == 2 :       # Here this is the corner case i.e., if weight is 2 then if we divide this into two parts then
        print("NO")   # each part will be of weight 1. But they likes even no.
    else:
        print("YES")
else:
    print("NO")