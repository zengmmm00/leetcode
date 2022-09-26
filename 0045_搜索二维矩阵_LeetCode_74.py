class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0]:
            return False
        r = 0
        for i in range(len(matrix)):
            if matrix[i][0] <= target:
                r = i
            else:
                break
        for i in range(len(matrix[r])):
            if matrix[r][i] == target:
                return True
        return False
