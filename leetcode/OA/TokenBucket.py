import time


class TokenBucket(object):

    def __init__(self, msPerToken, maxToken):
        self._msPerToken = msPerToken
        self._maxToken = maxToken
        self._start_time = int(time.time() * 1000)
        self._totalNums = 0

    def worker(self):
        if self._totalNums >= self._maxToken:
            return

        stop_time = int(time.time() * 1000)
        time_interval = stop_time - self._start_time
        while time_interval >= self._msPerToken:
            self._totalNums += 1
            time_interval -= self._msPerToken
            if self._totalNums == self._maxToken:
                break
        print("worker - totalTokens:", self._totalNums)
        self._start_time = int(time.time() * 1000)

    def acquireTokens(self, numTokens):
        self.worker()
        if numTokens >= self._maxToken:
            self._totalNums = 0
            return self._maxToken
        elif self._totalNums >= numTokens:
            res = numTokens
            self._totalNums -= numTokens
            return res
        elif self._totalNums < numTokens:
            res = self._totalNums
            self._totalNums = 0
            return res
        return -1


tb = TokenBucket(100, 5)
time.sleep(0.1)
time.sleep(0.45)
print(tb.acquireTokens(3))  # expect 3
print(tb.acquireTokens(2))  # expect 2
print(tb.acquireTokens(1))  # expect 0
time.sleep(0.35)
print(tb.acquireTokens(1))  # expect 1
