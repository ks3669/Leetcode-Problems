'''
The below solution will be of time complexity o m(log n) where M is the number of rows and N is the number of columns
Because we have 1 for loop which iterates through teh rows and we have a binary search solution which will go through the columns hence logN
'''
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



'''
The below code runs at o log(m*n) because the binary search is applied to both rows and columns
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        while (low <= high) :
            mid = low + (high - low) // 2
            if (target >= matrix[mid][0]) and (target <= matrix[mid][-1]):
                low1 = 0
                high1 = len(matrix[mid])
                while( low1 <= high1):
                    mid1 = low1 + (high1 - low1) // 2
                    if matrix[mid][mid1] == target:
                        return True
                    elif matrix[mid][mid1] > target:
                        high1 = mid1 - 1
                    else:
                        low1 = mid1 + 1
                return False
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
