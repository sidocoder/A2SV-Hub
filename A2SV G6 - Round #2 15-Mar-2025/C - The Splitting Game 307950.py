# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

def solve():
    t = int(input())  
    
    for _ in range(t):
        n = int(input())  
        s = input().strip()  
        
        
        prefix_distinct = [0] * (n + 1)
        seen = set()
        for i in range(n):
            seen.add(s[i])
            prefix_distinct[i + 1] = len(seen)
        
        
        suffix_distinct = [0] * (n + 1)
        seen = set()
        for i in range(n - 1, -1, -1):
            seen.add(s[i])
            suffix_distinct[i] = len(seen)
        
        
        max_value = 0
        for i in range(1, n):
            max_value = max(max_value, prefix_distinct[i] + suffix_distinct[i])
        
        print(max_value)


solve()
