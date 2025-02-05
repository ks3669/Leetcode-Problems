class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        # Bottom-up DP approach (modifying the matrix in place)
        for row in range(n - 2, -1, -1):  # Start from second last row
            for col in range(n):
                # Consider three possible moves: left-diagonal, down, right-diagonal
                left = matrix[row + 1][col - 1] if col > 0 else float('inf')
                down = matrix[row + 1][col]
                right = matrix[row + 1][col + 1] if col < n - 1 else float('inf')

                # Update the current cell with the minimum sum path
                matrix[row][col] += min(left, down, right)

        # The answer is the minimum value in the first row
        return min(matrix[0])
