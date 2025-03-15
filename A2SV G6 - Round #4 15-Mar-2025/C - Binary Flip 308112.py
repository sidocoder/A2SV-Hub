# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C


t = int(input())

for _ in range(t):
    n = int(input())
    a = input()
    b = input()

    balance = 0
    flip_positions = set()
    
    for i in range(n):
        balance += 1 if a[i] == '1' else -1
        if balance == 0:
            flip_positions.add(i)

    flipped = False
    possible = True

    for i in range(n - 1, -1, -1):
        if flipped:
            if a[i] == b[i]:
                if i not in flip_positions:
                    possible = False
                    break
                flipped = False
        else:
            if a[i] != b[i]:
                if i not in flip_positions:
                    possible = False
                    break
                flipped = True

    print("YES" if possible else "NO")
