class HouseRobber(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        last, now = 0, 0
        for num in nums:
            last, now = now, max(last + num, now)

        def inner():
            print(now)
        inner()
        dir = (0,1),(1,0),(-1,0),(0, -1)
        print(type(dir))
        for i,j in dir:
            print("%s,%s" %(i,j))
        return now


HouseRobber = HouseRobber()
HouseRobber.rob([1,3,5,7])



