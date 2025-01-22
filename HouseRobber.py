class Solution:
    def rob(self, nums: List[int]) -> int:
        # If there are no houses, the maximum money is 0
        if not nums:
            return 0
        
        # If there's only one house, rob it
        if len(nums) == 1:
            return nums[0]
        
        # Initialize two variables to store the maximum amount robbed up to the previous house
        prev1 = 0  # Money robbed from the house before the previous one
        prev2 = 0  # Money robbed from the previous house
        
        # Iterate through each house
        for num in nums:
            # Calculate the maximum amount by either robbing this house or skipping it
            current = max(prev2, prev1 + num)
            
            # Update prev1 and prev2 for the next iteration
            prev1 = prev2
            prev2 = current
        
        # The result is stored in prev2
        return prev2
