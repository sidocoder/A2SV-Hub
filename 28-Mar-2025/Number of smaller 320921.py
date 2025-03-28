# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n,m=[int(i) for i in input().split()]
arr1=[int(i) for i in input().split()]
arr2 = [int(i) for i in input().split()]
i = 0
ans = []
for num in arr2:
    while i < n and arr1[i] < num:
        i += 1
    ans.append(i)
print(*ans)
    