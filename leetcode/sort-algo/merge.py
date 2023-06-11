from typing import List


def mergesort(nums: List[int], low, high):
    if low < high:  # index, not the list size
        middle = int(low + (high - low) / 2)
        nums_left = mergesort(nums[low:middle + 1], 0, middle - low)
        nums_right = mergesort(nums[middle + 1:], 0, high - middle - 1)
        return merge(nums_left, nums_right)
    else:
        return [nums[0]]


# sorted list of var1 and var2
def merge(var1, var2):
    len1, len2 = len(var1), len(var2)
    curr, var1_, var2_ = 0, 0, 0
    nums = []
    while curr < len1 + len2 and var1_ < len1 and var2_ < len2:
        if var1[var1_] < var2[var2_]:
            nums.append(var1[var1_])
            var1_ += 1
        else:
            nums.append(var2[var2_])
            var2_ += 1
    # if var1_ < len1:
    #     ret += var1[var1_:]
    # if var2_ < len2:
    #     ret += var2[var2_:]
    nums += var1[var1_:] or var2[var2_:]
    return nums


arr = [5, 2, 9, 1, 6, 7]
ret = mergesort(arr, 0, len(arr) - 1)
print(ret)
