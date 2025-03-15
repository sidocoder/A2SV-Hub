# Problem: B - Nafargi's Binary Reduction Game - https://codeforces.com/gym/594077/problem/B

from collections import Counter
n = int(input())
str = input()

count_one = str.count('1')
count_zero = len(str) - count_one
if count_one == count_zero:
    print(0)
else:
    print(abs(count_one - count_zero))
