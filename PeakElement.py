class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If the middle element is less than the element to its right,
            # then the peak lies in the right half.
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                # Otherwise, the peak is in the left half (including mid).
                right = mid
        
        # When left == right, we've found a peak.
        return left
