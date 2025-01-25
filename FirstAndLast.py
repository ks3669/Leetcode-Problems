class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Helper function to find the first (leftmost) position of 'target'
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    # Even if we find target, continue searching left to find the first occurrence
                    if nums[mid] == target:
                        index = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return index

        # Helper function to find the last (rightmost) position of 'target'
        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    # Even if we find target, continue searching right to find the last occurrence
                    if nums[mid] == target:
                        index = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return index

        # Use the helper functions to get first and last positions
        first_pos = findFirst(nums, target)
        last_pos = findLast(nums, target)

        return [first_pos, last_pos]
