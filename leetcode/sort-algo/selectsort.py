from typing import List


def bubblesort(nums: List[int]):
    for i in range(0, len(nums) - 1):
        flag = True
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j] and flag:
                nums[i], nums[j] = nums[j], nums[i]

    return nums


arr = [5, 2, 9, 1, 6, 7, 19]
print(bubblesort(arr))
