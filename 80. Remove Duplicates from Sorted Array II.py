# Solution 1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        k = 2 
        for i in range(2, len(nums)):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        return k
        



# Solution 2
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        start_p = 1
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                cnt += 1
            else:
                cnt = 0
            if cnt < 2:
                nums[start_p] = nums[i]
                start_p += 1
        return start_p


# Solution 3
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        for num in nums:
            if i < 2 or num != nums[i - 2]:
                nums[i] = num
                i += 1
        return i
    
