# Problem: B - Fix the Forecast! - https://codeforces.com/gym/591928/problem/B

from collections import defaultdict, deque, Counter
import sys
input = sys.stdin.readline
def read_int(): return int(input().strip())
def read_string(): return input().strip()
def read_int_list(): return list(map(int, input().split()))
def read_char_list(): return list(input().strip())
def read_map(): return map(int, input().split())
def read_matrix(n, m): return [list(map(int, input().split())) for _ in range(n)]

for _ in range(read_int()):
    n, k = read_map()
    arr_a = read_int_list()
    arr_b = read_int_list()

    hashh = defaultdict(deque)  
    arr = sorted(arr_a)
    arr_b.sort()
    
    for a, b in zip(arr, arr_b):
        hashh[a].append(b)  
    
    ans = []
    
    for val in arr_a:
        ans.append(hashh[val].popleft())  
    
    print(*ans)  
