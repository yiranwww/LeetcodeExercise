class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return nums[0]

        max_left = [0] * n
        max_right = [0] * n

        max_left[0] = 0
        for i in range(1, n):
            max_left[i] = max(max_left[i-1] + nums[i-1], 0)
        
        max_right[n-1] = 0
        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1] + nums[i+1], 0)
        
        max_sum = float('-inf')
        for i in range(n):
            max_sum = max(max_sum, max_left[i] + max_right[i] + nums[i])
        
        return max_sum
