import math
import numpy as np
from numpy import random


class createTypes(object):

    def evenListInteger(self, n):
        return [i for i in range(0, n, 2)]

    def evenListString(n):
        return [str(i) for i in range(0, n, 2)]

    def prime(self, n):
        return [num for num in (2, n) if self.isPrime(num)]

    def isPrime(self, n):
        for i in range(1, int(math.sqrt(n))):
            if n % i == 0:
                return False
            else:
                return True

    def func1(self, list):
        return [0 if i % 2 == 0 else 1 for i in list]

    # 矩阵转置 matrix transposition
    def transposeMatrix(self, matrix):
        mat = random.random(size=(2, 4))
        n, m = mat.shape
        return [[row[col] for row in mat] for col in range(m)]

    def createSet(self, set):
        # set = {1,2,3,4,5,6,5,4,3,2,1}
        return {i ** 2 for i in set}

    # 生成字典
    def createDict1(self):
        student = {}
        for i in range(20):
            student["student" + str(i)] = random.randint(60, 100)
        return student

    # return {"student"+str(i):random.randint(60,90) for i in range(20)}
    def filterDict(dic):
        highscore = {}
        for name, score in dic.items():
            if score > 90:
                highscore[name] = score
        return highscore
        return {name: score for name, score in dict.items if score > 90}

    # 随机生成电影清单
    def dict(self):
        ret = {}
        for i in range(10):
            films = set([])
            for film in random.randint(4, 10):
                films.add("film" + str(film))
            ret["user" + i] = films
        return ret
        return {"user" + str(index): {"film" + str(filmItem) for filmItem in random.randint(4, 10)} for index in
                range(10)}

    def exchangeKeyValue(self, dict):
        return {[v, u] for u, v in dict.items()}

    # 大小写计数合并 : key值最终全部为小写
    def count(self, dict):
        return {k.lower: dict.get(k.lower, 0) + dict.get(k.upper, 0) for k, v in dict.items()}
