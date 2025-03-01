class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def helper(i):
            if i == -1:
                nums.reverse()
                return

            if nums[i] < nums[i + 1]:
                swap_i = len(nums) - 1
                while nums[swap_i] <= nums[i]:
                    swap_i -= 1
                
                nums[i], nums[swap_i] = nums[swap_i], nums[i]

                nums[i + 1:] = reversed(nums[i + 1:])
                return
            helper(i - 1)
        helper(len(nums) - 2)
