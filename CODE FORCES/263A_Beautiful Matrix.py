# https://codeforces.com/problemset/problem/263/A


row, column = 0, 0
for i in range(5):
    lis = list(map(int, input().split()))
    for j in range(len(lis)):
        if lis[j] == 1:
            row, column = i + 1 , j + 1
            break
print(abs(row - 3) + abs(column - 3))   # Here i was printing the output inside the loop so the answer was not getting
                                        # accepted.
