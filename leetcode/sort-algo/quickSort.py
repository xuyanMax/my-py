from typing import List


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[0]
        less = [i for i in nums[1:] if i <= pivot]
        greater = [i for i in nums[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def quicksort_2(nums: List[int], low, high):
    if low < high:
        pivot = partition(nums, low, high)
        quicksort_2(nums, low, pivot - 1)
        quicksort_2(nums, pivot + 1, high)
    return nums


def partition(nums: List[int], low: int, high: int):
    pivot = nums[high]
    curr = low
    for i in range(low, high):
        if nums[i] <= pivot:
            nums[curr], nums[i] = nums[i], nums[curr]
            curr += 1
    nums[curr], nums[high] = nums[high], nums[curr]
    return curr


arr = [5, 2, 9, 1, 6, 7]
# sorted_arr = quicksort(arr)
sorted_arr2 = quicksort_2(arr, 0, len(arr) - 1)
# print(sorted_arr)
print(sorted_arr2)

