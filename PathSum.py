class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        
        # Dynamic programming: modify the matrix in-place
        # Each cell in row i accumulates the minimum path sum up to that point
        for i in range(1, n):
            for j in range(n):
                # The value directly above
                best = matrix[i - 1][j]
                
                # Check the diagonal above-left (if in bounds)
                if j > 0:
                    best = min(best, matrix[i - 1][j - 1])
                
                # Check the diagonal above-right (if in bounds)
                if j < n - 1:
                    best = min(best, matrix[i - 1][j + 1])
                
                # Accumulate the minimum path sum into the current cell
                matrix[i][j] += best
        
        # The answer is the minimum value in the last row
        return min(matrix[-1])
