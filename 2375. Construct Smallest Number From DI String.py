class Solution:
    def check(self, number, pattern):
        for index in range(len(pattern)):
            if (pattern[index] == "I" and number[index] > number[index + 1]):
                return False
            elif (pattern[index] == "D" and number[index] < number[index + 1]):
                return False
        return True

    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        # generate sequence
        number_seq = "".join(str(num) for num in range(1, n + 2))

        for permutation in permutations(number_seq):
            permutation_str = "".join(permutation)
            if self.check(permutation_str, pattern):
                return permutation_str
            
        return ""

# permutations function:https://www.geeksforgeeks.org/permutation-and-combination-in-python/
# start from the smallest automatically.

