# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

def min_kicks(s):
    def simulate(s, favor_team):
        a_score = b_score = 0
        a_remain = b_remain = 5
        for i in range(10):
            if i % 2 == 0:
                a_remain -= 1
                if s[i] == '1' or (s[i] == '?' and favor_team == 0):
                    a_score += 1
            else:
                b_remain -= 1
                if s[i] == '1' or (s[i] == '?' and favor_team == 1):
                    b_score += 1
            if a_score > b_score + b_remain or b_score > a_score + a_remain:
                return i + 1
        return 10

    return min(simulate(s, 0), simulate(s, 1))

t = int(input())
for _ in range(t):
    s = input().strip()
    print(min_kicks(s))
