# Problem: A - Nth Digit in Sequence - https://codeforces.com/gym/588468/problem/A

# 

def nth_digit(n):
    length = 1  
    count = 9   
    start = 1   
    while n > length * count:
        n -= length * count
        length += 1
        count *= 10
        start *= 10

    number = start + (n - 1) // length  
    digit_index = (n - 1) % length      

    return int(str(number)[digit_index])  


n = int(input())
print(nth_digit(n))
