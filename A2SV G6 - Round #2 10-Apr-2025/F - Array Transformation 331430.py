# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import Counter
from collections import defaultdict

n = int(input())  
for _ in range(n):
    length = int(input())  
    nums = list(map(int, input().split()))  

    count = Counter(nums)
    count_values = Counter(count.values())
    
    # 1:1 , 2:2 , 3:3 6:2
    # 2:2 1:1 3: 1
    if len(set(count_values.values())) == 1:
        maxx_occurence = max(count_values, key=count_values.get)
    else:
        maxx_occurence = max(count_values.values())
    deleted = 0
    for val in count.values():
        if val < maxx_occurence:
            deleted += 1
        elif val > maxx_occurence:
            diff = val - maxx_occurence
            deleted += diff
            
    
    print(deleted)
