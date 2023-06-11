from collections import Counter
import sys
import time
# from iteration_utilities import deepflatten
import random


class trick(object):
    # 反转字符串
    def reverse(self, s):
        return s[::-1]

    # 首字母大写
    def capitalize(self, s):
        return s.title()

    # 在字符串中查找唯一元素
    def uniqueElements(self, s):
        tmp_set = set(s)
        new_string = ''.join(tmp_set)
        return new_string

    # n 次打印字符串或列表
    def printNTimes(self, str, list, n):
        print(str * n)
        print(list * n)

    # 列表推导式
    def updateList(self, list):
        newList = [2 * x for x in list]
        return newList

    # 变量交换
    def swap(self, a, b):
        a, b = b, a
        print(a)
        print(b)

    # 将字符串拆分为子字符串列表
    def splitter(self, str, deliminator):
        return str.split(deliminator)

    # 将字符串列表组合成单个字符串
    def concatenate(self, list, joiner):
        return joiner.join(list)

    # 检查回文字符串
    def validPalindrome(self, str):
        return str == str[::-1]

    # 列表中的元素统计
    def count(self, list):
        return Counter(list)

    # 查找两个字符串是否为字母
    def isAnagram(self, str1, str2):
        count1 = Counter(str1)
        count2 = Counter(str2)
        return count1 == count2

    # 使用 try-except-else 块
    def trycatch(self, a, b):
        try:
            print(a / b)
        except ZeroDivisionError:
            print("Division by zero")
        else:
            print("no exception raised")
        finally:
            print("finally...")

    # 使用枚举获取索引 / 值对
    def en(self, list):
        for index, value in enumerate(list):
            print('{0}:{1}'.format(index, value))

    # 检查对象的内存使用情况
    def checkMemory(self, object):
        print(sys.getsizeof(object))

    # 合并两个字典
    def combineDict(self, dict1, dict2):
        return {**dict1, **dict2}

    # 计算运行时间
    def calculateProgramTime(self):
        start = time.time()
        a, b = 1, 2
        c = a + b
        print((time.time() - start) * 10 * 6)  # microsecond

    #
    def flatten1d(self, list):
        return [item for sublist in list for item in sublist]

    #
    def sample(self, list, num_sample):
        return random.sample(list, num_sample)

    def int2List(self, num):
        # return [int(x) for x in str(num)]
        return list(map(int, str(num)))

    # 以下函数将检查列表中的所有元素是否唯一。
    def unique(self, list):
        return len(list) == len(set(list))

    def createDicByTwoLists(self, list1, list2):
        # list1 = [1, 2, 3, 4]
        # list2 = ['a','b','c','d','e']
        return dic(zip(list1, list2))


trick = trick()
print(trick.reverse("asd"))
print(trick.capitalize("asd shuo slasdn sa"))
print(trick.uniqueElements("asdasdasdasddddskjkkjjkzxcmnbzvwiuerwqsssssjasdnbxnbcz"))
trick.printNTimes("abc", [1, 2, 3], 3)
trick.printNTimes("abc", [0], 3)
print([0] * 3)
print(trick.updateList([1, 2, 3, 4]))
trick.swap(1, 2)
print(trick.splitter("abc asdm sds asd pfneisa adsow", " "))
print(trick.splitter("sample/ string 2", "/"))
print(trick.concatenate(["my", "name", "is", "xu"], " "))
print(trick.concatenate(["my", "name", "is", "xu"], "-"))
print(trick.validPalindrome("asdsa"))
print(trick.validPalindrome("asdfghgfdsag"))

count = trick.count(['a', 'a', 'b', 'c', '/', 'd', 'e', 'e'])
print(count.values())
print(count.items())
print(count.keys())
print(count.get('a'))
str_1, str_2, str_3 = "acbde", "abced", "abcda"
print(trick.isAnagram(str_1, str_2))
print(trick.isAnagram(str_1, str_3))
print(trick.isAnagram(str_3, str_2))
trick.trycatch(10, 0)
trick.trycatch(10, 4)
trick.en(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
trick.checkMemory(list)
trick.checkMemory(int)
trick.checkMemory(bool)
trick.checkMemory(object)
trick.checkMemory(24)
trick.checkMemory("aaa/")
dict_1 = {'apple': 9, 'banana': 6}
dict_2 = {'banana': 4, 'orange': 8}
print(trick.combineDict(dict_1, dict_2))
trick.calculateProgramTime()
print(trick.flatten1d([[1, 2, 3], [3]]))

x, y = input().split()  # 使用打包功能，一行输入两个整数并用空格隔开
print(x == y)
