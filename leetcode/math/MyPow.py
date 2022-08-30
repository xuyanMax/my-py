class MyPow(object):
    def myPow0(self, x: float, n: int) -> float:
        return pow(x, n)

    def myPow1(self, x: float, n: int) -> float:
        if not n:
            return 1
        if n < 0:
            return self.myPow(1 / x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)

    def myPowIter(self, x: float, n: int) -> float:
        if  n < 0:
            n = -n
            x = 1/x
        pow = 1
        while n:
            if n&1:
                pow = pow * x
            x *= x
            n >> 1
        return pow
