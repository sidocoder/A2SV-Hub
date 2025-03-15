# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

n, m = map(int, input().split())
a = list(map(int, input().split()))

damage_right = [0] * n
damage_left = [0] * n

for i in range(1, n):
    damage_right[i] = damage_right[i - 1] + max(0, a[i - 1] - a[i])

for i in range(n - 2, -1, -1):
    damage_left[i] = damage_left[i + 1] + max(0, a[i + 1] - a[i])

for _ in range(m):
    s, t = map(int, input().split())
    if s < t:
        print(damage_right[t - 1] - damage_right[s - 1])
    else:
        print(damage_left[t - 1] - damage_left[s - 1])
