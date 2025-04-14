# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
b = list(map(int, sys.stdin.readline().strip().split()))

if sum(a) != sum(b):
    print(-1)
    exit()

p1, p2 =0, 0

cur_sum1, cur_sum2 = 0, 0

ans = 0

while p1 < n:
    
    cur_sum1 += a[p1]
    cur_sum2 += b[p2]
    p1 += 1
    p2 += 1

    while cur_sum1 != cur_sum2:
        if cur_sum1 < cur_sum2:
            cur_sum1 += a[p1]
            p1 += 1
        else:
            cur_sum2 += b[p2]
            p2 += 1
    ans += 1
print(ans)