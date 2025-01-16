class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize two pointers for binary search
        left, right = 0, len(nums) - 1

        # Perform binary search
        while left <= right:
            # Calculate the mid-point
            mid = (left + right) // 2

            # Check if the target is at mid
            if nums[mid] == target:
                return mid

            # Determine if the left half is sorted
            if nums[left] <= nums[mid]:
                # Check if the target lies within the left sorted range
                if nums[left] <= target < nums[mid]:
                    # Narrow the search to the left half
                    right = mid - 1
                else:
                    # Narrow the search to the right half
                    left = mid + 1
            else:
                # The right half is sorted
                # Check if the target lies within the right sorted range
                if nums[mid] < target <= nums[right]:
                    # Narrow the search to the right half
                    left = mid + 1
                else:
                    # Narrow the search to the left half
                    right = mid - 1

        # If the target is not found, return -1
        return -1
