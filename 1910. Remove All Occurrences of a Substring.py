class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_len = len(part)

        for char in s:
            stack.append(char)
            
            if len(stack) >= part_len and ''.join(stack[-part_len:]) == part:
                # remove the last len(part) from stack
                for _ in range(part_len):
                    stack.pop()
        return "".join(stack)



## a tricky solution
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, "", 1)  # Replace only the first occurrence of part
        return s
