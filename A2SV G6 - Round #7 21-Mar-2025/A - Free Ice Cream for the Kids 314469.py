# Problem: A - Free Ice Cream for the Kids - https://codeforces.com/gym/596141/problem/A

t, first = map(int, input().split())  
remain = first
distressed = 0

for _ in range(t):
    sign, n = input().split()
    n = int(n)

    if sign == '+':
        remain += n
    elif sign == '-' and n <= remain:
        remain -= n
    else:
        distressed += 1  

print(remain, distressed)
