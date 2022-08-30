# Explaination.
# Take number X for example, 10011001.
# Divide it in 2 parts:
# <1>the last digit ( 1 or 0, which is " i&1 ", equivalent to " i%2 " )
# <2>the other digits ( the number of 1, which is " f[i >> 1] ", equivalent to " f[i/2] " )


class CountingBits(object):

    def sol(self, num):
        dp = [0] * len(num+1)
        for i in range(1, num+1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp;