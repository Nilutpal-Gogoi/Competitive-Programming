# You are given the array a consisting of n positive (greater than zero) integers.
#
# In one move, you can choose two indices i and j (i≠j) such that the absolute difference between ai and aj is no more
# than one (|ai−aj|≤1) and remove the smallest of these two elements. If two elements are equal, you can remove any of
# them (but exactly one).
#
# Your task is to find if it is possible to obtain the array consisting of only one element using several (possibly,
# zero) such moves or not.
#
# You have to answer t independent test cases.
#
# Input
# The first line of the input contains one integer t (1≤t≤1000) — the number of test cases. Then t test cases follow.
#
# The first line of the test case contains one integer n (1≤n≤50) — the length of a. The second line of the test case
# contains n integers a1,a2,…,an (1≤ai≤100), where ai is the i-th element of a.
#
# Output
# For each test case, print the answer: "YES" if it is possible to obtain the array consisting of only one element using
# several (possibly, zero) moves described in the problem statement, or "NO" otherwise.
#
# Example
# inputCopy
# 5
# 3
# 1 2 2
# 4
# 5 5 5 5
# 3
# 1 2 4
# 4
# 1 3 4 4
# 1
# 100
# outputCopy
# YES
# YES
# NO
# NO
# YES
# Note
# In the first test case of the example, we can perform the following sequence of moves:
#
# choose i=1 and j=3 and remove ai (so a becomes [2;2]);
# choose i=1 and j=2 and remove aj (so a becomes [2]).
# In the second test case of the example, we can choose any possible i and j any move and it doesn't matter which
# element we remove.
#
# In the third test case of the example, there is no way to get rid of 2 and 4.


t = int(input())
for _ in range(t):
    n = int(input())
    lis = list(map(int, input().split()))
    lis.sort()
    temp = []
    print(n)
    for i in range(n):
        temp.append(lis[i])
    for i in range(1, n):
        if lis[i]-lis[i-1]<=1:
            temp.remove(lis[i-1])
    if len(temp) == 1:
        print("YES")
    else:
        print("NO")           # Here we have used an extra space

# efficient one - The basic idea we can think of is that if we found any two number having difference more than one then
# we directly print NO because we won't be able to delete both the numbers BUT in question it is asked print YES we can
# return a list with only one element.


for _ in range(int(input())):
    n = int(input())
    l = sorted(map(int, input().split()))
    while (len(l)>1) and l[1]-l[0]<=1:
        l.pop(0)
    if len(l)==1:
        print("YES")
    else:
        print("NO")


for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    answer = "YES"
    for i in range(1,n):
        if l[i]-l[i-1] > 1:
            answer = "NO"
            break
    print(answer)