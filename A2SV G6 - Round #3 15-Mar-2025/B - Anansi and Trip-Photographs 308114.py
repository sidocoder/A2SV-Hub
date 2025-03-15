# Problem: B - Anansi and Trip-Photographs - https://codeforces.com/gym/588468/problem/B

def arrange(row, target_difference, heights):
    heights.sort()  
    front = heights[:row]  
    back = heights[row:]   

    for i in range(row):
        if back[i] - front[i] < target_difference:
            return "NO"
    return "YES"

t = int(input())  
results = []
for _ in range(t):
    r, x = map(int, input().split())  
    heights = list(map(int, input().split()))  
    results.append(arrange(r, x, heights))

print("\n".join(results))
