class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        cur_res = 0
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                res += nums[i]
            else:
                cur_res = max(cur_res, res)
                res = nums[i]
        
        return max(cur_res, res)

    # 处理类似问题考虑一个临时比较值
