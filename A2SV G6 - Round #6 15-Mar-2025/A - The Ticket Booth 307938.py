# Problem: A - The Ticket Booth - https://codeforces.com/gym/594077/problem/A

n, s = map(int,input().split())

# count = 0
# while s > 0:
#     if s < n:
#         s = 0
#         count += 1
#     else:
#         s -= n
#         count += 1
count = (s + n - 1) // n
print(count)