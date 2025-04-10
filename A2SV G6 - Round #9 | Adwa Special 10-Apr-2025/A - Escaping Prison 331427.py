# Problem: A - Escaping Prison - https://codeforces.com/gym/601269/problem/A

t = int(input())


for _ in range(t):
    n,h = map(int, input().split())
    query = []
    for _ in range(n):
        w,l = map(int, input().split())
        query.append(max(w,l))
       
    
    if sum(query) >= h:
        print('YES')
    else:
        print('NO')

       

    # _sum = sum(_max)
    
    


