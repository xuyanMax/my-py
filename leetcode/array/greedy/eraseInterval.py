def eraseOverlapInterval(intvs: list[list[int]]):
    n = len(intvs)
    count = 0
    # sorted by end time
    intvs.sort(lambda x: x[1])
    x_end = intvs[0][1]
    for intv in intvs:
        if intv[0] >= x_end:
            count += 1
            x_end = intv[1]
    # 用总区间数 - 最多非重叠区间数 = 需要移除的区间数量
    return n - count
