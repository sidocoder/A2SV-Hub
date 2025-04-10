# Problem: B - Empress Taytu and The Water Source - https://codeforces.com/gym/601269/problem/B

def is_valid(s, demand, time, k):
    total_time = 0
    for i in range(len(demand)):
        trips = (demand[i] + s - 1) // s 
        total_time += trips * time[i]
        if total_time > k:
            return False
    return True

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    demand = list(map(int, input().split()))
    time = list(map(int, input().split()))

    left = 1
    right = max(demand)
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        if is_valid(mid, demand, time, k):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)
