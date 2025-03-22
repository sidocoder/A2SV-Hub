# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n, s = map(int, input().split())
arr=list(map(int, input().split()))

left,right = 0,0
summ,max_length = 0,0

while right < n:
    summ += arr[right]
    while summ > s and left <= right:        
        summ -= arr[left]
        left += 1
    
    max_length = max(max_length,right -left + 1)
    right += 1
print(max_length) 
    
 

