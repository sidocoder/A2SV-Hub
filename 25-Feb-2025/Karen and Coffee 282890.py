# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

def coffee_brewing():
    r, k, q = map(int, input().split())

    MAX_TEMPERATURE = 200000
    freq = [0] * (MAX_TEMPERATURE + 2)

    for _ in range(r):
        s, e = map(int, input().split())
        freq[s] += 1
        freq[e + 1] -= 1

    for i in range(1, MAX_TEMPERATURE + 1):
        freq[i] += freq[i - 1]

    admissible = [0] * (MAX_TEMPERATURE + 1)
    for i in range(1, MAX_TEMPERATURE + 1):
        if freq[i] >= k:
            admissible[i] = 1

    admissible_prefix = [0] * (MAX_TEMPERATURE + 1)
    for i in range(1, MAX_TEMPERATURE + 1):
        admissible_prefix[i] = admissible_prefix[i - 1] + admissible[i]

    results = []
    for _ in range(q):
        c, d = map(int, input().split())
        results.append(str(admissible_prefix[d] - admissible_prefix[c - 1]))

    print("\n".join(results))

coffee_brewing()
