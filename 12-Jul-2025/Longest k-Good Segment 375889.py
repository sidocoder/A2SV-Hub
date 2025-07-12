# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict
def longest_k_good_segment(n, k, a):
    freq = defaultdict(int)
    l, max_len, best_l, best_r, distinct_count = 0, 0, 0, 0, 0

    for r in range(n):
        if freq[a[r]] == 0:
            distinct_count += 1
        freq[a[r]] += 1

        while distinct_count > k:
            freq[a[l]] -= 1
            if freq[a[l]] == 0:
                distinct_count -= 1
            l += 1

        if r - l + 1 > max_len:
            max_len = r - l + 1
            best_l, best_r = l, r

    print(best_l + 1, best_r + 1)


n, k = map(int, input().split())
a = list(map(int, input().split()))

longest_k_good_segment(n, k, a)
