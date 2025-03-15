# Problem: B - Special Matrix Quest - https://codeforces.com/gym/586960/problem/B

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
mid = n // 2

sum_good = 0

for i in range(n):
    sum_good += matrix[i][i]
    sum_good += matrix[i][n - 1 - i]

for i in range(n):
    sum_good += matrix[mid][i]
    sum_good += matrix[i][mid]

sum_good -= matrix[mid][mid] * 3

print(sum_good)
