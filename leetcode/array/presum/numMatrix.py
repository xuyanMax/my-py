class numMatrix(object):

    def __init__(self, matrix):
        self.matrix = matrix
        m = len(matrix)
        n = len(matrix[0])
        self.presum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, len(self.presum)):
            for j in range(1, len(self.presum[0])):
                self.presum[i][j] = self.presum[i - 1][j] + self.presm[i][j - 1] - self.presum[i - 1][j - 1] + \
                                    matrix[i - 1][j - 1]

    def sumRange(self, x1, x2, y1, y2):
        return self.presum[x2 + 1][y2 + 1] - self.presum[x2 + 1][y1] - self.presum[x1][y2 + 1] + self.presum[x1][y1]
