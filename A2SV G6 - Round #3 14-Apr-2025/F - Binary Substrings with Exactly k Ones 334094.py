# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

k = int(input())
nums = input()
n = len(nums)

def atmostk(k):
    if k == -1:
        return 0
    
    left = 0 
    count = 0
    ans = 0

    for right in range(n):
        if nums[right] == "1":
            count += 1  

       
        while count > k:
            if nums[left] == "1":
                count -= 1  
            left += 1 
        
        
        ans += right - left + 1
    
    return ans 


print(atmostk(k) - atmostk(k-1)) 