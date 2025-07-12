# Problem: Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

def largestNumber(nums,n):
    odd=[i for i in nums if i%2==1]
    even=[i for i in nums if i%2==0]
    if n==len(odd) or n==len(even):
        return nums
    # s = [str(i) for i in nums]
    nums.sort()
    
        
    return nums
n=int(input())
nums=[int(i) for i in input().split()]
print(*largestNumber(nums,n))
