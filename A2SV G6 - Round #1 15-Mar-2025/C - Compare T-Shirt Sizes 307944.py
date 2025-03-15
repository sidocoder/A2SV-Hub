# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585107/problem/C

def solve(a,b):
    if a[-1]>b[-1]:
        return '<'
    if a[-1]<b[-1]:
        return '>'
    
    n,m = len(a),len(b)
    if n==m:
        return '='
    if n>m and a[-1] == 'S':
        return '<'
    if n<m and a[-1]=='S':
        return '>'
    if n>m:
        return '>'
    if n<m:
        return'<'
    


for i in range(int(input())):
    a,b = input().split()
    print(solve(a,b))