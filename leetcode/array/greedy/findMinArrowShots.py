# 区间边界接触属于重叠，一只箭可刺穿所有重叠区间，求问所需箭头数，即非重叠区间个数

def findMinArrowShots(intvs: list[list[int]]):
    if len(intvs) == 0:
        return -1
    # intvs.sort(key=lambda x:x[1])
    sorted_by_endTime = sorted(intvs, key=lambda x: x[1])
    count = 0
    x_end = intvs[0][1]
    for intv in sorted_by_endTime:
        start = intv[0]
        # 区间边界接触算重叠
        if start > x_end:
            count += 1
            x_end = intv[1]
    return count
