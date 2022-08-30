class ThreeSum(object):
    # List[int] -> List[List[int]]
    @staticmethod
    def solution(nums):
        nums.sort()
        ret = []
        for i in range(len(nums) - 2):
            if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                left, right, s = i + 1, len(nums) - 1, -nums[i]
                while left < right:
                    if (nums[left] + nums[right]) == s:
                        ret.append((nums[i], nums[left], nums[right]))
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while right > left and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif (nums[left] + nums[right]) < s:
                        left += 1
                    else:
                        right -= 1
        return ret
