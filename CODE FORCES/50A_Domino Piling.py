# https://codeforces.com/problemset/problem/50/A


m, n = map(int, input().split())
temp = m*n
print(temp//2)


# Tutorial
# Answer is floor(N*M*0.5). Since there is N*M cells on the board and each domino covers exactly two of them we cannot
# place more for sure. Now let's show how to place exactly this number of dominoes. If N is even, then place M rows of
# N/2 dominoes and cover the whole board. Else N is odd, so cover N-1 row of the board as shown above and put floor(M/2)
# dominoes to the last row. In the worst case (N and M are odd) one cell remains uncovered.


