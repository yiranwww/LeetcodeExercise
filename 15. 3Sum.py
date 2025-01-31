class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            one = nums[i]
            left, right = i+1, n-1
            while left < right:
                cur_sum = one + nums[left] + nums[right]
                if cur_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left -1] and left < right:
                        left += 1
                elif cur_sum < 0:
                    left += 1
                else:
                    right -= 1
        return res
