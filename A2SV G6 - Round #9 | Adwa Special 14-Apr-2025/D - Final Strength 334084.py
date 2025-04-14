# Problem: D - Final Strength - https://codeforces.com/gym/601269/problem/D

def mergeSort(arr,l,r):
    if l == r:
   	 return
    
    # get the mid point of the current array and merge sort it
    mid = (l + r)//2
    mergeSort(arr,l,mid)
    mergeSort(arr,mid + 1, r)
    # merge the two halves after sorting them and calculating the answer
    merge(arr,l,mid,r)
 
def merge(arr,l,mid, r):
    # wins array to hold the number of wins each team have
 
    wins = [0]*(r - l + 1)
    # array to hold merged list
    merged = []
    
    # calculate the wins for the first group
    ptr = mid + 1
 
    # for every element of the first group
    for i in range(l,mid + 1):
   	 # move the second groups point to an element which is greater or equal to it
  	 
   	 while ptr <= r and arr[ptr][1] < arr[i][1]:
   		 ptr += 1
 
   	 # the total numbe of wins for the current element
   	 #is the nubmer of element in the second group
   	 #that is lower than it
   	 wins[i - l] = ptr - (mid + 1)
 
    # same thing for the second group
    ptr = l
    for i in range(mid + 1,r+1):
   	 while ptr <= mid and arr[ptr][1] < arr[i][1]:
   		 ptr += 1
   	 wins[i - l] = ptr - l
 
    # merge the two groups based on the new value
    pt1 = l
    pt2 = mid + 1
 
    while pt1 <= mid or pt2 <= r:
   	 if (pt2 > r) or (pt1 <= mid and arr[pt1][1] + wins[pt1 - l] < arr[pt2][1] + wins[pt2 - l]):
   		 arr[pt1][1] += wins[pt1 - l]
   		 merged.append(arr[pt1])
   		 pt1 += 1
   	 else:
   		 arr[pt2][1] += wins[pt2 - l]
   		 merged.append(arr[pt2])
   		 pt2 += 1
 
    arr[l:r + 1] = merged
 
 
 
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr = [[i,j] for i,j in enumerate(arr)]
    mergeSort(arr,0,2**n - 1)
    ans = [i[1] for i in sorted(arr,key = lambda x: x[0])]
    
    print(*ans)
 
t = int(input())
for _ in range(t):
    solve()