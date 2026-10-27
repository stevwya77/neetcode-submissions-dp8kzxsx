class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev = []
        for num in nums:
            if num not in prev:
                prev.append(num)
            else:
                return True
        return False