class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc_length = 1
        dec_length = 1
        n = len(nums)
        res = 1

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                inc_length += 1
                dec_length = 1
            elif nums[i] < nums[i-1]:
                inc_length = 1
                dec_length += 1
            else:
                inc_length = 1
                dec_length = 1
            res = max(res, inc_length, dec_length)
        
        return res
