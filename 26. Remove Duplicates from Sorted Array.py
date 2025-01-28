class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                cnt += 1
            else:
                nums[i-cnt] = nums[i]
        return n - cnt
