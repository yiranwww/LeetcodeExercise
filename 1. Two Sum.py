# Use a dictionary. The index and the corresponding value
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        res = {}
        for i in range(n):
            cur = nums[i]
            goal = target - cur
            if goal in res:
                return [res[goal], i]
            else:
                res[cur] = I


# dict = {}
# dict['one'] = "this is one"
# dict[2] = "this is two"
# print(dict['one']) = "this is one"
# print(dict[2]) = "this is two
