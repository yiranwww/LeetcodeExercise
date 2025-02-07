class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        n = len(queries)

        res = []
        color = {}

        ball = {}

        for cur_ball, cur_color in queries:
            
            if cur_ball in ball:
                pre_color = ball[cur_ball]
                color[pre_color] -= 1
                if color[pre_color] == 0:
                    del color[pre_color]

            ball[cur_ball] = cur_color
            color[cur_color] = color.get(cur_color, 0) + 1

            res.append(len(color))
        return res
