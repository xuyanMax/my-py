from collections import deque, defaultdict
class LFUCache:

    def __init__(self, capacity: int):
        self.keyToVal = {}
        self.keyToFreq = {}
        self.freToKeys = defaultdict(deque)
        self.cap = capacity
        self.minFreq = 0

    def get(self, key: int) -> int:
        if key not in self.keyToVal:
            return -1
        self.increaseFreq(key)
        return self.keyToVal[key]

    def increaseFreq(self, key: int):
        fre = self.keyToFreq[key]
        self.keyToFreq[key] = fre + 1
        s = self.freToKeys[fre]
        s.remove(key)

        self.freToKeys.setdefault(fre + 1, deque())
        self.freToKeys[fre + 1].appendleft(key)
        if not self.freToKeys[fre]:
            del self.freToKeys[fre]
            if fre == self.minFreq:
                self.minFreq += 1

    def put(self, key: int, val: int) -> int:
        if self.cap <= 0:
            return
        if key in self.keyToVal:
            self.keyToVal[key] = val
            self.increaseFreq(key)
            return

            # capacity less than the total number of keys
        if self.cap <= len(self.keyToVal):
            self.removeMinFreKey()

        self.keyToVal[key] = val
        self.keyToFreq[key] = 1
        self.freToKeys.setdefault(1, deque())
        self.freToKeys[1].appendleft(key)

        self.minFreq = 1

    def removeMinFreKey(self):
        minFreq = self.minFreq
        s = self.freToKeys[minFreq]
        print(s)
        deletedKey = s.pop()
        print(deletedKey)
        if not s:
            del self.freToKeys[minFreq]
        del self.keyToVal[deletedKey]
        del self.keyToFreq[deletedKey]


lfu = LFUCache(2)
lfu.put(2, 1)
lfu.put(3, 2)
lfu.get(3)
lfu.get(2)
