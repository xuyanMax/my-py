from typing import List


def canPartition(self, nums: List[int]):
    W = sum(nums)
    if W % 2 != 0:
        return
    W = W >> 1
    dp = [False] * (W + 1)
    N = len(nums)
    dp[0] = True
    # sort in place
    nums.sort()
    for i in range(0, N):
        for j in range(W, -1, -1):
            print(i, j, nums[i])
            if j >= nums[i]:
                dp[j] = dp[j - nums[i]] or dp[j]
    return dp[W]
