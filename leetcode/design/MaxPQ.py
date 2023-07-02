class MaxPQ():
    def __init__(self, cap: int):
        self.pq = [None] * (cap + 1)
        self.size = 0

    def max(self):
        # return max
        return self.pq[1]

    # add new element to the bottom and swim it
    def insert(self, e) -> None:
        self.size += 1
        self.pq[self.size] = e
        self.swim(self.size)

    # swap the max element to the bottom and sink the new top one
    def delMax(self):
        max = self.pq[1]
        self.swap(1, self.size)
        self.pq[self.size] = None
        self.size -= 1
        self.sink(1)
        return max

    def swim(self, index) -> None:
        # 1-based index, not 0-based.
        while self.parent(index) >= 1 and self.pq[index] > self.pq[self.parent(index)]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def sink(self, index) -> None:
        while self.left(index) <= self.size:
            max = self.left(index)
            if self.right(index) <= self.size and self.pq[max] < self.pq[self.right(index)]:
                max = self.right(index)
            if self.pq[max] < self.pq[index]:
                break  # parent node is greater
            self.swap(index, max)
            index = max

    def swap(self, i, j) -> None:
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

    def left(self, index: int) -> int:
        return index * 2

    def right(self, index: int) -> int:
        return index * 2 + 1

    def parent(self, index: int) -> int:
        return index // 2
