# Problem: C - Escape-Proof Transfers - https://codeforces.com/gym/591928/problem/C

n, t, c = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
left = 0

for right in range(n):
    if nums[right] > t:
        left = right + 1
    elif right - left + 1 == c:
        count += 1
        left += 1

print(count)
