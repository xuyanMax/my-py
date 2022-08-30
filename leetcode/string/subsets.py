class subsets:
    # Input: nums = [1, 2, 3]
    # Output:
    # [
    #     [3],
    #     [1],
    #     [2],
    #     [1, 2, 3],
    #     [1, 3],
    #     [2, 3],
    #     [1, 2],
    #     []
    # ]
    # : List[int]) -> List[List[int]]
    def subsets(self, nums):
        ret = []
        self.dfs(nums, [], ret)
        return ret

    def dfs(self, nums, pref, ret):
        ret.append(pref)
        for i in range(len(nums)):
            self.dfs(nums[i + 1:], pref + [nums[i]], ret)

    def subsets2(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        return res