# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

def min_removal(m, s):
    def is_palindrome(s):
        return s == s[::-1]
    
    if is_palindrome(s):
        return 0

    unique_chars = set(s)
    min_removal = float('inf')

    for char in unique_chars:
        l, r = 0, m - 1
        removals = 0

        while l < r:
            if s[l] == s[r]:  
                l += 1
                r -= 1
            elif s[l] == char:  
                removals += 1
                l += 1
            elif s[r] == char:  
                removals += 1
                r -= 1
            else:  
                removals = float('inf')
                break

        min_removal = min(min_removal, removals)
    if min_removal != float('inf'):
        return min_removal 
    else:
        return -1
    


n = int(input())
results = []
for _ in range(n):
    m = int(input())
    s = input().strip()
    results.append(str(min_removal(m, s)))

print("\n".join(results))
