class maxContinousSum:
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)

    def maxSubArray2(self, nums):
        len = len(nums)
        dp = [0] * len
        res = dp[0] = nums[0]

        for i in range(1, len):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            res = max(res, dp[i])

        return res


mc = maxContinousSum();
print(mc.maxSubArray([1,2,3,4,5,-2,4]))