# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

from collections import defaultdict

class Solution:
    def totalFruit(self, fruits):
        fruit_count = defaultdict(int)
        window_start = 0
        max_fruits = 0

        for window_end in range(len(fruits)):
            fruit_count[fruits[window_end]] += 1

            while len(fruit_count) > 2:
                fruit_count[fruits[window_start]] -= 1
                if fruit_count[fruits[window_start]] == 0:
                    del fruit_count[fruits[window_start]]
                window_start += 1

            max_fruits = max(max_fruits, window_end - window_start + 1)

        return max_fruits
