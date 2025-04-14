# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

n = int(input())
points = [int(i) for i in input().split()]
points.sort()

suml = 0
sumr = sum(points)
min_distance = float("inf")
answer = points[0]

for i, point in enumerate(points):
    left_side_distance = (point * i - suml)
    right_side_distance = sumr - (n - i) *  point
    current_total_distance = left_side_distance + right_side_distance
    if min_distance > current_total_distance:
        min_distance = current_total_distance
        answer = point

    suml += point
    sumr -= point

print(answer)