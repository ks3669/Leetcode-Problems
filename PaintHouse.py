class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        We can solve this in O(n) time by doing an in-place dynamic programming:
        
        For each house i, to paint it a certain color j, we add the minimum
        cost among the other two colors of house i-1. This ensures no two
        adjacent houses share the same color.
        
        Example:
            costs = [
              [17, 2, 17],
              [16, 16, 5],
              [14, 3, 19]
            ]
            Output should be 10: (2 + 5 + 3)

        Steps (in-place update):
          costs[i][0] += min(costs[i-1][1], costs[i-1][2])
          costs[i][1] += min(costs[i-1][0], costs[i-1][2])
          costs[i][2] += min(costs[i-1][0], costs[i-1][1])

        Then at the end, the answer is min(costs[-1]), i.e., the cheapest color choice for the last house.
        """

        if not costs:
            return 0

        n = len(costs)
        for i in range(1, n):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])

        return min(costs[-1])
