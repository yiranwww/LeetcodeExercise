class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        cnt = 0
        for i in range(n):
            if nums[i] == 0:
                cnt += 1
            else:
                nums[i - cnt] = nums[i]
        
        while cnt > 0:
            nums[n - cnt] = 0
            cnt -= 1
