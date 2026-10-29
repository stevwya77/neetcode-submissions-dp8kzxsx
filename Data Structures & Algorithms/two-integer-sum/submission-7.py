class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            n_find = target - nums[i]
            if n_find in seen:
                return [seen[n_find], i]
            seen[nums[i]] = i