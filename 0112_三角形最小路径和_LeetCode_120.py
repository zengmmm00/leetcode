class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        layer = [triangle[0][0]]
        for i in range(1, len(triangle)):
            tmp = []
            tmp.append(layer[0] + triangle[i][0])
            for j in range(1, i):
                tmp.append(min(layer[j - 1], layer[j]) + triangle[i][j])
            tmp.append(layer[-1] + triangle[i][-1])
            layer = tmp
        return min(layer)
