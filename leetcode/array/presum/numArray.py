class numArray(object):
    def __init__(self, nums):
        self.presum = [0] * (len(nums) + 1)
        for i in range(1, len(self.presum)):
            print(i)
            self.presum[i] = self.presum[i - 1] + nums[i - 1]

    def rangeQuery(self, left, right):
        return self.presum[right] - self.presum[left]


nums = [1, 2, 3, 4, 5]
numArray = numArray(nums)
print("from index 2 to 3:", numArray.rangeQuery(2, 3 + 1))
