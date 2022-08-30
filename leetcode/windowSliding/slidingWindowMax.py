import collections


def maxSlidingWindow(nums, k):
    deq = collections.deque
    res = []
    for i, val in enumerate(nums):
        # remove smaller numbers than nums[i]
        while deq and nums[deq[-1]] < val:
            deq.pop()  # pop tail
        # remove indexes out of range k
        if deq[0] == i - k:
            deq.popleft()
        deq += i
        # deq.append(i)
        if i >= k - 1:
            res[i - k + 1] = nums[deq[0]]
    return res


print(maxSlidingWindow([1, 2, 3], 3))
