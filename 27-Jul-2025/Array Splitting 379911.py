# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == n:
    print(0)
else:
    diff = []
    for i in range(n - 1):
        diff.append(a[i + 1] - a[i])
    
    diff.sort(reverse=True)
    total_gap = sum(diff[:k - 1])  
    total_cost = a[-1] - a[0] - total_gap
    print(total_cost)
