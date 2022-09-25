# invts[[]]
intvs = [[1, 10], [2, 3], [3, 4], [5, 7]]


def intervalSchedule(intvs: list[list[int]]):
    if len(intvs) == 0:
        return -1
    # intvs.sort(key=lambda x:x[1])
    sorted_by_endTime = sorted(intvs, key=lambda x: x[1])
    count = 0
    x_end = intvs[0][1]
    for intv in sorted_by_endTime:
        start = intv[0]
        # 区间边界接触不算重叠
        if start >= x_end:
            count += 1
            x_end = intv[1]
    return count


intervalSchedule(intvs)
