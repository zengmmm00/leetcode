class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: (x[1], x[0]))
        c = 1
        a = points[0][1]
        for i in range(1, len(points)):
            p = points[i]
            if p[0] <= a <= p[1]:
                continue
            else:
                c += 1
                a = p[1]
        return c
