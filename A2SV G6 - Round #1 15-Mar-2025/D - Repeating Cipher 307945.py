# Problem: D - Repeating Cipher - https://codeforces.com/gym/585107/problem/D

num = int(input())
word = input()
result = ''
j = 1
i = 0
while i<len(word):
    result += word[i]
    i+=j
    j+=1

print(result)
