'''
The below code will give me a time complexity of about o(log n) because at each point the array is sliced to its half size.
It is simple binary search wth conditions modified where we compare the mid value with low value and high value considering some edge cases and then doing the same concept of Binary search of slicing the array each time
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = low + (high - low) // 2
            min_value = nums[mid]
            if low == high:
                return min(min_value,nums[low])
            elif nums[mid] > nums[high]:
                low = mid + 1
            elif (nums[mid] < nums[high]) and (nums[mid] >= nums[low]):
                high = mid
            elif (nums[mid] < nums[high]) and (nums[mid] < nums[low]):
                high = mid
