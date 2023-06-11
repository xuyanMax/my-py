class Node:
    def __init__(self, k: int, v: int):
        self.key = k
        self.val = v
        self.next = None
        self.pre = None


class DoubleList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0

    def addLast(self, x: Node):
        self.tail.pre.next = x
        x.pre = self.tail.pre
        x.next = self.tail
        self.tail.pre = x
        self.size += 1

    def remove(self, x: Node):
        x.pre.next = x.next
        x.next.pre = x.pre
        self.size -= 1

    def removeFirst(self) -> Node:
        if self.head == self.tail:
            return None
        first = self.head.next
        self.remove(first)
        return first

    def size(self) -> int:
        return self.size


class LRUCache:
    map: dict[int, Node]
    cache: DoubleList
    capacity: int

    def __init__(self, capacity: int):
        self.cache = DoubleList()
        self.map = {}
        self.capacity = capacity

    def put(self, key: int, val: int):
        if key in self.map:
            # update new val
            self.map[key].val = val
            self.makeRecently(key)
            return
        if self.capacity == self.cache.size:
            self.removeLeastRecently()
        self.addRecently(key, val)

    def get(self, key: int):
        if key in self.map:
            self.makeRecently(key)
            return self.map.get(key).val
        else:
            return None

    def makeRecently(self, key: int):
        # update the key to the latest
        x = self.map.get(key)
        self.cache.remove(x)
        self.cache.addLast(x)

    def addRecently(self, key: int, val: int):
        # add new key,val pair to map and doublelist
        x = Node(key, val)
        self.map[key] = x
        # self.cache.append(x)
        self.cache.addLast(x)

    def removeLeastRecently(self):
        # both from doublelist and map
        first = self.cache.removeFirst()
        self.map.pop(first.key)

    def deleteKey(self, key: int):
        x = self.map.get(key)
        self.cache.remove(x)
        self.map.pop(key)  # remove it from map


if __name__ == '__main__':
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    lru.get(1)
    lru.put(3, 3)
    print(lru.get(1))
    print(lru.get(2))
    print(lru.get(3))
