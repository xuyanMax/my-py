import time


class TokenBucket(object):

    def __init__(self, msPerToken, maxToken):
        self.msPerToken = msPerToken
        self.maxToken = maxToken
        self.start_time = int(time.time() * 1000)
        self.totalNums = 0

    def worker(self):
        if self.totalNums >= self.maxToken:
            return

        stop_time = int(time.time() * 1000)
        time_interval = stop_time - self.start_time
        while time_interval >= self.msPerToken:
            self.totalNums += 1
            time_interval -= self.msPerToken
            if self.totalNums == self.maxToken:
                break
        print("worker - totalTokens:", self.totalNums)
        self.start_time = int(time.time() * 1000)

    def acquireTokens(self, numTokens):
        self.worker()
        if numTokens >= self.maxToken:
            self.totalNums = 0
            return self.maxToken
        elif self.totalNums >= numTokens:
            self.totalNums -= numTokens
            return numTokens
        elif self.totalNums < numTokens:
            res = self.totalNums
            self.totalNums = 0
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
