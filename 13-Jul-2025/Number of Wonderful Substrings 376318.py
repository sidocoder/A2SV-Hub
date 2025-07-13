# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # hashh = {'a': 1, 'b': 2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10}

        # subset = []
        # for num in range(2 ** len(word)):
        #     temp = []
        #     for i in range(32):
        #         if num & (1 << i) != 0:
        #             temp.append(word[i])
        #     subset.append(temp)

#-----------------------------------------------------------------
        # count = 0
        # for i in range(len(subset)):
        #     if len(subset[i]) == 1:
        #         count += 1
        #     else:
        #         pre = [0]
        #         curr = 0
        #         for j in range(len(subset[i])):
        #             curr ^= hashh[subset[i][j]]
        #             pre.append(curr)
        #         if pre[-1] == 0 or pre[-1] == 1:
        #             count += 1
        # return count - 1
#-------------------------------------------------

        # n = len(word)
        # valid_count = 0

        # for i in range(n):
        #     freq = Counter()
        #     odd_count = 0

        #     for j in range(i, n):
        #         char = word[j]
        #         freq[char] += 1

        #         if freq[char] % 2 == 1:
        #             odd_count += 1
        #         else:
        #             odd_count -= 1

        #         if odd_count <= 1:
        #             valid_count += 1

        # return valid_count
#----------------------------------------------------------
        prefix_count = defaultdict(int)
        prefix_count[0] = 1 

        mask = 0
        count = 0

        for ch in word:
            bit = ord(ch) - ord('a')
            mask ^= (1 << bit) 

            
            count += prefix_count[mask]

            for i in range(10): 
                count += prefix_count[mask ^ (1 << i)]

            prefix_count[mask] += 1

        return count


                        








            

