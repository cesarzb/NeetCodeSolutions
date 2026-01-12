# Contains Duplicate - https://neetcode.io/problems/duplicate-integer/question

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen: return True
            else: seen.add(num)
        
        return False

# bonus one liner solution
# return len(set(nums)) != len(nums)
