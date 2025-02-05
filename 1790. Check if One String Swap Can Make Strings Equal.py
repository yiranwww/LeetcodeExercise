class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if set(s1) != set(s2):
            return False


        res = 0
        cnt_1 = []
        cnt_2 = []
      # Here cannot be cnt_1 = cnt_2 = []
      # if do so, the cnt_1 and cnt_2 will be the same in the next update step
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                cnt_1.append(s1[i])
                cnt_2.append(s2[i])
                res += 1
        
      # pay attention to the str.sort() [change the original] and sorted(str) [keeps the original]  
      if (res == 0) or (res == 2) and (sorted(cnt_1) == sorted(cnt_2)):
            return True
        else:
            return False
