# Problem: Limited Repainting - https://codeforces.com/contest/2070/problem/C

def min_penalty(n, k, s, a):
    def can_do(x):
        segments = 0
        i = 0
        while i < n:
            if s[i] == 'B' and a[i] > x:
                segments += 1
                j = i
                while j < n and not (s[j] == 'R' and a[j] > x):
                    j += 1
                i = j
            else:
                i += 1
        return segments <= k

    low, high = 0, max(a)
    while low < high:
        mid = low + (high - low) // 2
        if can_do(mid):
            high = mid
        else:
            low = mid + 1
    return low

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    a = list(map(int, input().split()))
    print(min_penalty(n, k, s, a))
