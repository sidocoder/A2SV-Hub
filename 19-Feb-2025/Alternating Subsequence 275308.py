# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

def max_alternating_subsequence(n, a):
    total_sum = 0
    max_element = a[0] 
    
    for i in range(1, n):
        if (a[i] > 0 and max_element > 0) or (a[i] < 0 and max_element < 0):
            
            max_element = max(max_element, a[i])
        else:
            total_sum += max_element
            max_element = a[i]
    
    total_sum += max_element
    return total_sum

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(max_alternating_subsequence(n, a))
