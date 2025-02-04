class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return res
        
        start_p = 0
        n = len(nums)
        
        for i in range(1, n):
            if nums[i] != nums[i - 1] + 1:
                # Add the range to the result
                if start_p == i - 1:
                    res.append(str(nums[start_p]))
                else:
                    res.append(str(nums[start_p]) + "->" + str(nums[i - 1]))
                start_p = i  # Update start_p for the new range
        
        # Handle the last range after the loop
        if start_p == n - 1:
            res.append(str(nums[start_p]))
        else:
            res.append(str(nums[start_p]) + "->" + str(nums[n - 1]))
        
        return res
