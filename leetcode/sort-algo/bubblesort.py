from typing import List


def bubblesort(nums: List[int]):
    for i in range(len(nums)):
        flag = False
        for j in range(len(nums) - 2, i - 1, -1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True
        if flag is False:
            break
    return nums


arr = [5, 2, 9, 1, 6, 7, 19]
print(bubblesort(arr))
