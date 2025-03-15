# Problem: A - A+ Student - https://codeforces.com/gym/590053/problem/A

# t = int(input())
# test_cases = []

# for _ in range(t):
#     a, b, c = map(int, input().split())
#     test_cases.append([a, b, c])  

# for arr in test_cases:
#     maximum = max(arr)
    
    
#     if arr[0] == arr[1] == arr[2]:
#         ans=[maximum - c + 1, maximum - c + 1, maximum - c + 1]
#     else:
#         ans = [(maximum - x + 1) if x != maximum else 0 for x in arr]

#     print(*ans)

t = int(input())  
for _ in range(t):
    a, b, c = map(int, input().split())  
    

    A = max(0, max(b, c) - a + 1)
    B = max(0, max(a, c) - b + 1)
    C = max(0, max(a, b) - c + 1)
    
   
    print(A, B, C)

