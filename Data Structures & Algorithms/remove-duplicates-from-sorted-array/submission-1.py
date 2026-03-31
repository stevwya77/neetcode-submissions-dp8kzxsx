class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                result.append(nums[i]);
        for num in range(len(result)):
            nums.remove(result[num]);
        return len(nums)