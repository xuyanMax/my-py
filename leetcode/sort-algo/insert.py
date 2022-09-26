class insert(object):
    def algo(self, nums):
        for i in range(1, len(nums)):
            if (nums[i - 1] > nums[i]):
                flag = nums[i]
                j = i - 1
                while j >= 0 and flag < nums[j]:
                    nums[j + 1] = nums[j]
                nums[j + 1] = flag
