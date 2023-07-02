from typing import List


def knapsack_01_2d(n: int, w: int, val: List[int], wt: List[int]):
    assert n == len(val)
    dp = [[0] * (w + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if j > wt[i - 1]:
                dp[i][j] = max(dp[i - 1][j - wt[i - 1]] + val[i - 1], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][w]


def knapsack_01_1d(n: int, w: int, val: List[int], wt: List[int]):
    assert n == len(val)
    dp = [0] * len(w + 1)
    for i in range(1, n + 1):
        for j in range(w, -1, j - 1):
            dp[j] = max(dp[j], dp[j - wt[i - 1]] + val[i - 1])

    return dp[w]


def complete_knapsack(amount: int, coins: List[int]) -> int:
    n = len(coins)
    dp = [0] * (amount + 1)
    dp[0] = 1  # base case
    for i in range(n):
        for j in range(1, amount + 1):
            if j - coins[i] >= 0:
                dp[j] = dp[j] + dp[j - coins[i]]

    return dp[amount]


def complete_knapsack_2d(amount: int, coins: List[int]) -> int:
    n = len(coins)
    dp = [[0] * (amount + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            if coins[i] <= j:
                dp[i][j] = dp[i - 1][j - coins[i]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][amount]
