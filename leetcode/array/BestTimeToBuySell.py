class BestTimeToBuySell(object):
    def solution(self, nums):
        if not nums:
            return 0
        min = nums[0]
        res = 0
        for num in nums[1:]:
            if num < min:
                min = num
            res = max(res, num - min)
        return res
