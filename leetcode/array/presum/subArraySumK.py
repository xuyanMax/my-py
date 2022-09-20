def subArraySum(nums, k):
    presum_map = {0: 1}
    res, presum = 0, 0
    for i in range(1, len(nums) + 1):
        presum += nums[i - 1]
        res += presum_map.get(presum - k, 0)
        presum_map[presum] = presum_map.get(presum, 0) + 1
    return res


nums = [1, 2, 3, 4, 5, 4, 3, 2]
print(subArraySum(nums, 3))
