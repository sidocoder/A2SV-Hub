# Problem: F - Nahom's Array Dilemma - https://codeforces.com/gym/594077/problem/F

def solve():
    n = int(input())
    a = list(map(int , input().split()) )
    def check(nums):
        pref = [0]
        stack = []
             
        for num in nums:
             pref.append(num + pref[-1])
        
        for i , num in enumerate(nums):
             while stack and num >= nums[stack[-1]]:
                 k = stack.pop()
                 sm = pref[i] - pref[k]
                 if sm > 0:
                    return False
            
             stack.append(i)
    
        return True
    
    if check(a) and check(a[::-1]):
             print("YES")
    else:
             print("NO")



t = int(input())

for _ in range(t):
    solve()