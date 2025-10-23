# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        def isprime(n):
            d = 2
            while d * d <= n:
                if n % d == 0:
                    return False

                d += 1
            return True


        if n < 2:
            return 0
        prime = [True for i in range(n)]
        prime[0] = prime[1] = False
        for i in range(2, math.ceil(math.sqrt(n))):
            if prime[i]:
                for j in range(i*i, n , i):
                    prime[j] = False
        return sum(prime)

        # count = 0
        # for i in range (2, n):
        #     if is_prime(i) and i < n:
        #         count += 1
        # return count