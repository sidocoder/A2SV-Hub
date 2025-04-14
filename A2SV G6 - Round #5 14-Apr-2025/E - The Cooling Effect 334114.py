# Problem: E - The Cooling Effect - https://codeforces.com/gym/591928/problem/E

def solve():
    t = int(input())
    for _ in range(t):
        while True:
            line = input()
            if line.strip():
                break
        n, k = map(int, line.split())

        while True:
            pos_line = input()
            if pos_line.strip():
                break
        pos = list(map(int, pos_line.split()))

        while True:
            temp_line = input()
            if temp_line.strip():
                break
        temp = list(map(int, temp_line.split()))

        cooling = [float('inf')] * n
        for i in range(k):
            cooling[pos[i] - 1] = temp[i]

        forward = [float('inf')] * n
        forward[0] = cooling[0]
        for i in range(1, n):
            forward[i] = min(forward[i - 1] + 1, cooling[i])

        backward = [float('inf')] * n
        backward[-1] = cooling[-1]
        for i in range(n - 2, -1, -1):
            backward[i] = min(backward[i + 1] + 1, cooling[i])

        result = [min(forward[i], backward[i]) for i in range(n)]
        print(*result)

solve()
