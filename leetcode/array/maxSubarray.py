# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution,
# try coding another solution using the divide and conquer approach, which is more subtle.

class maxSubarray:
    # @param A, a list of integers
    # @return an integer
    # 6:57
    def maxSubArray(self, A):
        if not A:
            return 0

        curSumEndHere = maxSumSoFar = A[0]
        for num in A[1:]:
            curSumEndHere = max(num, curSumEndHere + num)
            maxSumSoFar = max(maxSumSoFar, curSumEndHere)

        return maxSumSoFar