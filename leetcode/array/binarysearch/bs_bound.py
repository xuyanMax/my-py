def bs_left_bound(nums, target):
    if target < nums[0]:
        return -1
    left, right = 0, len(nums) - 1

    # which exit condition - left == right +1
    # left检索范围是[0, nums.length-1]
    while left <= right:
        mid = left + (right - left) / 2
        if nums[mid] == target:  # go for left bound
            right = mid - 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    # 检查出界情况
    # 特殊情况: 当target比nums中所有元素都大，会出现left数组越界, right == nums.length -1 && left == nums.length;
    #         当target比nums中所有元素都小，会出现right数组越界，right == -1 && left == 0
    return -1 if left >= len(nums) or nums[left] != target else left


def bs_right_bound(nums, target):
    if target > nums[-1]:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) / 2
        if nums[mid] == target:  # 收缩左侧边界
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    # 越界处理right 越界, 当所有nums元素比target小，right == -1； 当所有nums元素比target大，
    return -1 if right < 0 or nums[right] != target else right
