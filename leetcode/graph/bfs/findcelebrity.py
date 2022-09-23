# 可以直接调用，能够返回 i 是否认识 j
def knows(i, j):
    return True


# 1:n people. return the celebrity
def findCelebrity(n):
    if n == 1:
        return 0
    queue = []
    for i in range(n):
        queue.append(i)
    while len(queue) > 1:
        candidate = queue.pop()
        other = queue.pop()
        if knows(candidate, other) or not knows(other, candidate):
            queue.append(other)
        else:
            queue.append(candidate)

    cand = queue.pop()
    for i in range(n):
        if i == candidate:
            continue
        if knows(cand, i) or not knows(i, cand):
            return False
    return True
