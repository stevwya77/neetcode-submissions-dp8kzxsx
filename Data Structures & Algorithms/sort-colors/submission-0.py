class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0]
        for num in nums:
            counts[num] += 1
        
        n_idx = 0
        for i in range(len(counts)):
            for n in range(0, counts[i]):
                nums[n_idx] = i
                n_idx += 1
                