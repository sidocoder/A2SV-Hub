# Problem: A - Make the Product Zero - https://codeforces.com/gym/586960/problem/A

n = int(input())  
numbers = list(map(int, input().split()))  

minimum = min(map(abs, numbers))  

print(minimum) 
