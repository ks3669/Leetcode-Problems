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
