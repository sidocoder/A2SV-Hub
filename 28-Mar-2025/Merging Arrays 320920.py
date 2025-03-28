# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n,m=[int(i) for i in input().split()]
arr1=[int(i) for i in input().split()]
arr2 = [int(i) for i in input().split()]
ans = []
i = 0
j = 0
while i <len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        ans.append(arr1[i])
        i += 1
    else:
       ans.append(arr2[j])
       j += 1
ans.extend(arr1[i:])
ans.extend(arr2[j:])
print(*ans)
                   




