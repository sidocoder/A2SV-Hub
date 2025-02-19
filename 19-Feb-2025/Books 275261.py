# Problem: Books - https://codeforces.com/contest/279/problem/B

n, t = map (int, input().split())
nums = list(map(int, input().split()))
# nums.sort()
cnt =0
left = 0
time = 0
for i in range(len(nums)):
    time += nums[i]
    while time > t:
        time -= nums[left]
        left += 1
    cnt = max(cnt, i-left+1)
   
print(cnt)
# print(nums)
