class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        q = collections.deque(["a", "b", "c"])
        happy_string = []

        while q:
            s = q.popleft()
            if len(s) == n:
                happy_string.append(s)
                continue
            for ch in "abc":
                if s[-1] != ch:
                    q.append(s + ch)
        return "" if k > len(happy_string) else happy_string[k-1]
