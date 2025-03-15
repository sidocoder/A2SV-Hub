# Problem: A - Nth Digit in Sequence - https://codeforces.com/gym/588468/problem/A

def find_nth_digit(n):
    seq = ""
    num = 1
    while len(seq) < n:
        seq += str(num)
        num += 1
    print(seq[n - 1])

n = int(input())
find_nth_digit(n)
