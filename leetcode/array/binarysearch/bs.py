# 如下两个版本，nums=[1,2,2,2,2,3], target=2, 此算法返回的索引为2，无法正确返回target的左侧边界，即索引1
def binarySearch(nums: list[int], target: int):
    left, right = 0, len(nums) - 1
    # 搜索区间[0, nums.length - 1]
    # while退出条件是: left == right + 1 => [right+1, right]
    while left <= right:
        mid = (int)(left + (right - left) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return -1


# 左闭右开区间
def binarySearch_2(nums: list[int], target: int):
    left, right = 0, len(nums)
    # 终止条件 left == right
    while left < right:
        mid = (int)(left + (right - left) / 2)
        if nums[mid] == target:
            break
        elif nums[mid] > target:
            right = mid  # 右侧开区间
        elif nums[mid] < target:
            left = mid + 1  # 左侧闭区间
    # 因为while退出条件为left==right,区间[left, left]没有被搜索过，此时如果直接返回-1是错误的，因此在最后return处打个补丁即可
    return left if nums[left] == target else -1


# leetcode 153
def findMinInRotatedArray(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] < nums[right]:
            return nums[left]
        mid = int((right + left) / 2)
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


def findMaxInRotatedArray(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] < nums[right]:
            return nums[right]
        mid = int((right + left) / 2)
        if nums[mid] <= nums[right]:
            right=mid-1
        else:
            left=mid
        return nums[left] #left==right
