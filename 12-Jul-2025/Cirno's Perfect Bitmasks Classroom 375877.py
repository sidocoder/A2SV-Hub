# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

t = int(input())
for _ in range(t):
    x = int(input())
    i = 1
    while True:
        if (i ^ x) > 0 and (i & x) >0:
            print(i)
            break
        i+=1

