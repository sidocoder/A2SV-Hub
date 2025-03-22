# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))

maxDeque = deque()
minDeque = deque()
l = 0
total = 0

for r in range(n):
    while maxDeque and a[maxDeque[-1]] <= a[r]:
        maxDeque.pop()
    maxDeque.append(r)
    while minDeque and a[minDeque[-1]] >= a[r]:
        minDeque.pop()
    minDeque.append(r)
    while a[maxDeque[0]] - a[minDeque[0]] > k:
        if maxDeque[0] == l:
            maxDeque.popleft()
        if minDeque[0] == l:
            minDeque.popleft()
        l += 1
    total += r - l + 1

print(total)
