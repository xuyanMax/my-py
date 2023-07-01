# On output staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
#
# Once you pay the cost, you can either climb one or two steps.
# You need to find minimum cost to reach the top of the floor,
# and you can either start from the step with index 0, or the step with index 1.
#
# Example 1:
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
# Example 2:
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].


class MinCostClimbingStairs(object):
    def solution(self, cost):
        if not cost:
            return 0
        size = len(cost)
        if size == 1:
            return cost[0]
        if size == 2:
            return min(cost[0], cost[1])
        pred2, pred, curr = 0, 0, 0

        for c in cost[2:]:
            curr = c + min(pred2, pred)
            pred2, pred = pred, curr
        return min(pred, pred2)

    def dp(self, cost):
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = min(cost[0], cost[1])

        for i in range(2, len(cost)):
            dp[i] = max(dp[i-2] + cost[i], dp[i-1])
        return dp[-1]

