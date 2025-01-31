class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == val:
                k += 1
            else:
                nums[i-k] = nums[i]
        return n-k
