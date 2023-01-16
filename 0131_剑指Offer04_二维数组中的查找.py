class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        while len(matrix) != 0 and len(matrix[0]) != 0:
            matrix = self.cutRow(matrix, target)
            if len(matrix) == 0 or len(matrix[0]) == 0:
                return False
            matrix = self.cutCol(matrix, target)
            if len(matrix) == 0 or len(matrix[0]) == 0:
                return False
            if matrix[0][-1] == target:
                return True
        return False

    def cutCol(self, matrix, target):
        new_matrix = []
        col = None
        for i in range(len(matrix[0])):
            if matrix[0][i] <= target:
                col = i
            else:
                break
        if col is None:
            return new_matrix
        for i in range(len(matrix)):
            new_matrix.append(matrix[i][:col + 1])
        return new_matrix

    def cutRow(self, matrix, target):
        new_matrix = []
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                new_matrix.append(matrix[i])
        return new_matrix
