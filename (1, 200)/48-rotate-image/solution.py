class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        
class Solution2(object):
    def rotate(self, matrix):
        matrix[:] = zip(*matrix[::-1])
        return matrix

