class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range (len(matrix)):
            if target < matrix[i][-1]:
                low = 0
                high = len(matrix[i])
                while(low <= high):
                    mid = low + (high - low) // 2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] > target:
                        high = mid - 1
                    else:
                        low = mid + 1
            elif target == matrix[i][-1]:
                return True
            else:
                continue
        return False
