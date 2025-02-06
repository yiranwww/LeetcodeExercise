class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = 1
        points.sort(key = lambda x: x[0])
        end = points[0][1]

        for cur in points:
            if cur[0] > end:
                res += 1
                end = cur[1]
            else:
                end = min(end, cur[1])
        
        return res

        
