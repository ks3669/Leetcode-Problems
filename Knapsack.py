"""
Optimized Python solution for the 0/1 Knapsack problem.

Time Complexity:
    O(N * W) where N is the number of items and W is the capacity of the bag.
Space Complexity:
    O(W), since we use a one-dimensional list (dp) of size (W+1) to store maximum profit values.
Data Structure Used:
    - List (dp): This is used to store the maximum profit achievable for each capacity from 0 to W.
      Using a 1D list instead of a 2D list optimizes the space requirement while still allowing
      us to iteratively build up the solution.

The approach is based on dynamic programming where we iterate through each item and update the dp list
from right to left to ensure that each item is only used once (0/1 knapsack).
"""

def knapsack(profits, weights, W):
    n = len(profits)
    # dp[w] will hold the maximum profit for capacity w
    dp = [0] * (W + 1)
    
    # Process each item
    for i in range(n):
        # Traverse the dp array backwards to prevent reusing the same item more than once.
        for w in range(W, weights[i] - 1, -1):
            # Only update if the item can fit in the current capacity
            dp[w] = max(dp[w], dp[w - weights[i]] + profits[i])
    
    return dp[W]
