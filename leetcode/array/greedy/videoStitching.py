from typing import List


def videoStitching(clips: list[list[int]], T: int):
    prev_end, end, count = -1, 0, 0
    for s, e in sorted(clips):
        if end >= T or s > end:
            break
        elif prev_end < s <= end:
            prev_end = end
            count += 1
        end = max(end, e)
    return count if e >= T else -1


def videoStitching_2(self, clips: List[List[int]], T: int) -> int:
    max_jumps = [0] * 101
    # Convert clips to the furthest point you can jump from each point. O(N)
    for l, r in clips:
        max_jumps[l] = max(max_jumps[l], r)

    # it is then output jump game
    res = lo = hi = 0
    while hi < T:
        lo, hi = hi, max(max_jumps[lo:hi + 1])
        if hi <= lo: return -1
        res += 1
    return res
# AC: 24 ms, beats 99%`
