# Problem: C - Sombody Else Wants Mumumu's Number - https://codeforces.com/gym/607625/problem/C

from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    freq = Counter(a)
    max_freq = max(freq.values())
    
    if max_freq > n - max_freq:
        print(2 * max_freq - n)
    else:
        print(n % 2)
