"""
Problem: Koko Eating Bananas
Link: https://neetcode.io/problems/eating-bananas/question

You have an array of numbers of bananas on each pile.
Calculate slowest possible speed of eating bananas so you 
manage to do that in at most h hours.
You can only go to next pile after hour finishes.
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = high

        while low <= high:
            k = (low + high) // 2 

            total = 0
            for pile in piles:
                total += math.ceil(pile / k)
            if total <= h:
                ans = k
                high = k -1
            else: low = k + 1
        
        return ans
