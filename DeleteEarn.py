def deleteAndEarn(nums):
    if not nums:
        return 0

    max_num = max(nums)
    counts = * (max_num + 1)

    for num in nums:
        counts[num] += num

    # I Applied the logic similar to house robber problem
    dp = * (max_num + 1)
    dp = counts

    for i in range(2, max_num + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + counts[i])

    return dp[max_num]
