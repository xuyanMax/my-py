class Candy(object):
    def sol(self, ratings):
        if not ratings:
            return
        print(ratings)
        val = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                val[i] = val[i - 1] + 1
        print(val)
        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                val[i - 1] = max(val[i - 1], val[i] + 1)
        print(val)
        return sum(val)


ca = Candy()
print(ca.sol([1, 0, 2, 2, 4, 1]))
