class insert(object):
    @staticmethod
    def algo(nums):
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                flag = nums[i]
                j = i - 1
                # nums[0:j] is sorted and try to insert nums[j] to a correct position
                while j >= 0 and flag < nums[j]:
                    nums[j + 1] = nums[j]
                    j -= 1
                nums[j + 1] = flag
