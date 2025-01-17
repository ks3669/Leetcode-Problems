
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Number of rows and columns
        rows, cols = len(matrix), len(matrix[0])
        
        # Initialize binary search pointers
        left, right = 0, rows * cols - 1

        # Perform binary search
        while left <= right:
            mid = (left + right) // 2
            # Convert the 1D index to 2D row and column
            mid_value = matrix[mid // cols][mid % cols]

            # Check if mid_value matches the target
            if mid_value == target:
                return True
            elif mid_value < target:
                # Narrow search to the right half
                left = mid + 1
            else:
                # Narrow search to the left half
                right = mid - 1

        # If not found, return False
        return False
