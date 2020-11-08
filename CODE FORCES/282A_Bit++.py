# https://codeforces.com/problemset/problem/282/A


# language has one variable, called x.
# there are two operations- ++ increases the value of variable x by 1 and -- decreases the value of x by 1


n = int(input())
count = 0
for _ in range(n):
    x = str(input())
    if x == "X++" or x == "++X":
        count += 1
    elif x == "X--" or x == "--X":
        count -= 1
print(count)