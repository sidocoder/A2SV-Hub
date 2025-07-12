# Problem: A - Can I Get Your Number ? - https://codeforces.com/gym/607625/problem/A

n = int(input())
strings = [input().strip() for _ in range(n)]

first = strings[0]
length = len(first)

prefix = 0
for i in range(length):
    current_char = first[i]
    for s in strings[1:]:
        if s[i] != current_char:
            print(prefix)
            exit()
    prefix += 1

print(prefix)
