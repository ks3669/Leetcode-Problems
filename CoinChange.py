from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        We use a dynamic programming (DP) approach to find the fewest number of coins 
        required to make up the given amount. The idea is:

        1. Create a DP array of length (amount + 1), where dp[i] represents 
           the fewest coins needed to make the value i.
        2. Initialize dp[0] = 0 (0 coins needed to make 0 amount) and set all other 
           values to a large number (e.g., amount+1).
        3. For each i from 1 to amount:
             - For each coin in coins:
                 - If coin <= i, update dp[i] = min(dp[i], 1 + dp[i - coin]).
        4. Finally, if dp[amount] is still a large number (meaning we couldn't 
           form the amount), return -1. Otherwise, return dp[amount].

        Time Complexity: O(N * A) where N = number of coins, A = amount.
        Space Complexity: O(A) for the DP array.
        """
        
        # Edge case: If amount is 0, no coins are needed.
        if amount == 0:
            return 0
        
        # Initialize DP array
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        # Build up the DP array
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # If we haven't updated dp[amount], it means it's not possible
        return dp[amount] if dp[amount] != amount + 1 else -1
