# Problem: A - Two Ranges - https://codeforces.com/gym/604781/problem/A

q = int(input())
for _ in range(q):
    l1,r1,l2,r2 = (map(int, input().split()))
    choosen = l1
    
    for i in range(l2,r2 +1):
        if i != choosen:
            choosen2 = i
            break
    print(choosen, choosen2)

   