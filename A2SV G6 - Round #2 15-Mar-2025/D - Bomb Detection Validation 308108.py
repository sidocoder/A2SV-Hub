# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for i in range(n):
    for j in range(m):
        if field[i][j] == '.':
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m and field[ni][nj] == '*':
                    print("NO")
                    exit()
        elif field[i][j].isdigit():
            expected_bombs = int(field[i][j])
            bomb_count = sum(1 for dx, dy in directions if 0 <= i + dx < n and 0 <= j + dy < m and field[i + dx][j + dy] == '*')
            if bomb_count != expected_bombs:
                print("NO")
                exit()

print("YES")
