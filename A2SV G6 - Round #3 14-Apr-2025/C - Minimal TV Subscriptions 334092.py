# Problem: C - Minimal TV Subscriptions - https://codeforces.com/gym/588468/problem/C

from collections import Counter, defaultdict, deque
t = int(input())  # Number of test cases
for _ in range(t):
    n, k, d = map(int, input().split())  # Read values for n, k, d
    arr = list(map(int, input().split()))  # Read the show schedule
    window = Counter(arr[:d])  # Initialize window with first 'd' shows
    ans = len(window)  # Track minimum unique shows
    
    for i in range(d, n):  # Slide the window through the array
        window[arr[i]] += 1  # Add new show to window
        window[arr[i - d]] -= 1  # Remove old show from window
        
        if window[arr[i - d]] == 0:  # Remove show from counter if it no longer exists in window
            del window[arr[i - d]]
        
        ans = min(ans, len(window))  # Update the minimum unique shows
    
    print(ans)  # Output the result for the test case

