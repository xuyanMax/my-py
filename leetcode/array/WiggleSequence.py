class WiggleSequence(object):
    # 如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为 摆动序列 。
    # #第一个差（如果存在的话）可能是正数或负数。仅有一个元素或者含两个不等元素的序列也视作摆动序列。

    def sol(self, array):
        length = 1
        # 0 初始态
        # 1 上升  nums[i] < nums[i+1]
        # -1 下降 nums[i] > nums[i+1]
        trend = 0
        for i in range(1, len(array)):
            if trend > 0 and array[i] < array[i - 1]:
                length += 1
                trend = -1
            elif trend < 0 and array[i] > array[i - 1]:
                length += 1
                trend = 1
        return length
