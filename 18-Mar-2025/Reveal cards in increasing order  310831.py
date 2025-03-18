# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        stack = deque()

        for i in range(len(deck) - 1, -1, -1):
            if not stack:
                stack.append(deck[i])
            else:
                last = stack.pop()
                stack.appendleft(last)
                stack.appendleft(deck[i])
        return list(stack)


        