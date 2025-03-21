# Problem: B - Increasing Sequence - https://codeforces.com/gym/596141/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    ans = []
    used = set()
    j = 1
    i = 0

    while i < len(nums):
        if nums[i] == j:
            add = j + 1
            ans.append(add)
            used.add(add)
            j = add + 1
            
        
        else:
            add = j
            if add in used:
                while add <= nums[i]:
                    add + 1
                    ans.append(add)
            else:
                ans.append(j)
            
                j += 1
        i += 1

    
    print(max(ans))



  
