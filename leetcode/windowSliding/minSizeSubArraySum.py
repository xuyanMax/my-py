# leetcode 209
# all positive numbers
import collections
import math


def windowSlide(nums, target):
    sums, left, min_len = 0, 0, math.inf
    for i in range(len(nums)):
        sums += nums[i]

        while sums >= target:
            min_len = min(min_len, i - left + 1)
            sums -= nums[left]
            left += 1

    return min_len if min_len != math.inf else 0


# leetcode 862
# positive/negative numbers
def windowSlideWithNegative(nums, target):
    # index, presum
    deque = collections.deque([[0, 0]])
    presum, min_len = 0, float('inf')
    for i, num in enumerate(nums):
        presum += num
        while deque and presum - deque[0][1] >= target:
            min_len = min(min_len, i - deque.popleft()[0] + 1)
        while deque and presum <= deque[-1][
            1]:  # ensure deque is in increasing order, comparing current presum with the ones from the entry of the deque. In this case, from right.
            deque.pop()  # pop right
        deque.append([i + 1, presum])  # append right
        # print(deque)
    return min_len if min_len < float("inf") else -1
