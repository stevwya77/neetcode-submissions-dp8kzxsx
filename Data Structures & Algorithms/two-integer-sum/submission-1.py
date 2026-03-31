class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_dict = {}
        for index, item in enumerate(nums):
            diff = target - item
            if diff in n_dict:
                return [n_dict[diff], index]
            n_dict[item] = index
        