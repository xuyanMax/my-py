import numpy as np

# https://blog.csdn.net/weixin_43721000/article/details/120504199
# 一维数组
num_list = np.array([1, 8, 2, 3, 10, 4, 5])
num_sorted_list = np.sort(num_list)
print(num_sorted_list)  # [ 1  2  3  4  5  8 10]

# 排序返回数组索引
num_list = np.array([1, 8, 2, 3, 10, 4, 5])
index_list = np.argsort(num_list)
print(index_list)  # [0 2 3 5 6 1 4]

# 一维数组逆序排序
num_list = np.array([1, 8, 2, 3, 10, 4, 5])
print(np.sort(-num_list))

# 二维数组
num_list = np.array([
    [1, 8, 2, 9],
    [8, 2, 4, 5],
    [2, 3, 7, 4],
    [1, 2, 3, 5]
])
ordered_list = np.sort(num_list, axis=0)  # axis=0 是按列排序
print(ordered_list)
# [[1 2 2 4]
#  [1 2 3 5]
#  [2 3 4 5]
#  [8 8 7 9]]

ordered_list = np.sort(num_list, axis=1)  # axis=1 是按行排序
print(ordered_list)
# [[1 2 8 9]
#  [2 4 5 8]a
#  [2 3 4 7]
#  [1 2 3 5]]

# 二维数组 索引排序
num_list = np.array([
    [1, 8, 2, 9],
    [8, 2, 4, 5],
    [2, 3, 7, 4],
    [1, 2, 3, 5]
])
ordered_list = np.argsort(num_list, axis=0)  # axis=0 是按列排序
print(ordered_list)
# [[0 1 0 2]
#  [3 3 3 1]
#  [2 2 1 3]
#  [1 0 2 0]]
ordered_list = np.argsort(num_list, axis=1)  # axis=1 是按行排序
print(ordered_list)
# [[0 2 1 3]
#  [1 2 3 0]
#  [0 1 3 2]
#  [0 1 2 3]]
