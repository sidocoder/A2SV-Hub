# Problem: C - Permutation Minimization - https://codeforces.com/gym/594077/problem/C

from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    nums = map(int, input().split())

    queue = deque()

    for num in nums:
        if queue and num < queue[0]:
            queue.appendleft(num)
        else:
            queue.append(num)
    print(*queue)
