# https://blog.csdn.net/weixin_43721000/article/details/120504199
# sorted 升序排序
num_list = [1, 8, 2, 3, 10, 4, 5]
ordered_list = sorted(num_list)
num_list.sort()

print(ordered_list)  # [1, 2, 3, 4, 5, 8, 10]
print(num_list)  # [1, 2, 3, 4, 5, 8, 10]

# sorted 降序排序
num_list = [1, 8, 2, 3, 10, 4, 5]
ordered_list = sorted(num_list, reverse=True)
print(ordered_list)  # [1, 2, 3, 4, 5, 8, 10]

# sort 降序排序
num_list = [1, 8, 2, 3, 10, 4, 5]
num_list.sort(reverse=True)
print(num_list)  # [1, 2, 3, 4, 5, 8, 10]

# 不想要排序后的值，想要排序后的索引，可以这样做
num_list = [1, 8, 2, 3, 10, 4, 5]
ordered_list = sorted(range(len(num_list)), key=lambda k: num_list[k])
print(ordered_list)  # [0, 2, 3, 5, 6, 1, 4]

# 字符串类型排序
str_list = ['1', '8', '2', '3', '10', '4', '5']
ordered_list = sorted(str_list)
print(ordered_list)  # ['1', '10', '2', '3', '4', '5', '8']

# 2d array
book_list = [
    ['北大马克思主义研究', '9787509728529', 2011],
    ['人的解放', '9787215064003', 2014],
    ['西方经典悦读 资本论', '9787200092882', 2012],
    ['列宁的一生', '9787501319343', 2013],
]

# sorted 按出版年升序排序
ordered_list = sorted(book_list, key=lambda book: book[2])
print(
    ordered_list)  # [['北大马克思主义研究', '9787509728529', 2011], ['西方经典悦读 资本论', '9787200092882', 2012], ['列宁的一生', '9787501319343', 2013], ['人的解放', '9787215064003', 2014]]

# sort 按出版年降序排序
book_list.sort(key=lambda book: book[2], reverse=True)
print(
    book_list)  # [['人的解放', '9787215064003', 2014], ['列宁的一生', '9787501319343', 2013], ['西方经典悦读 资本论', '9787200092882', 2012], ['北大马克思主义研究', '9787509728529', 2011]]

# sorted 获取排序后的索引
book_list = [
    ['北大马克思主义研究', '9787509728529', 2011],
    ['人的解放', '9787215064003', 2014],
    ['西方经典悦读 资本论', '9787200092882', 2012],
    ['列宁的一生', '9787501319343', 2013],
]
ordered_list = sorted(range(len(book_list)), key=lambda k: book_list[k][2])
print(ordered_list)  # [0, 2, 3, 1]

# 字典数组排序
book_list = [
    {'name': '北大马克思主义研究', 'isbn': '9787509728529', 'publish_year': 2011},
    {'name': '人的解放', 'isbn': '9787215064003', 'publish_year': 2014},
    {'name': '西方经典悦读 资本论', 'isbn': '9787200092882', 'publish_year': 2012},
    {'name': '列宁的一生', 'isbn': '9787501319343', 'publish_year': 2013},
]
# sorted 按出版年降序排序
ordered_list = sorted(book_list, key=lambda book: book['publish_year'], reverse=True)
print(
    ordered_list)  # [{'name': '人的解放', 'isbn': '9787215064003', 'publish_year': 2014}, {'name': '列宁的一生', 'isbn': '9787501319343', 'publish_year': 2013}, {'name': '西方经典悦读 资本论', 'isbn': '9787200092882', 'publish_year': 2012}, {'name': '北大马克思主义研究', 'isbn': '9787509728529', 'publish_year': 2011}]
# sort 按出版年升序排序
book_list.sort(key=lambda book: book['publish_year'])
print(
    book_list)  # [{'name': '北大马克思主义研究', 'isbn': '9787509728529', 'publish_year': 2011}, {'name': '西方经典悦读 资本论', 'isbn': '9787200092882', 'publish_year': 2012}, {'name': '列宁的一生', 'isbn': '9787501319343', 'publish_year': 2013}, {'name': '人的解放', 'isbn': '9787215064003', 'publish_year': 2014}]

# 获取字典数据排序索引

book_list = [
    {'name': '北大马克思主义研究', 'isbn': '9787509728529', 'publish_year': 2011},
    {'name': '人的解放', 'isbn': '9787215064003', 'publish_year': 2014},
    {'name': '西方经典悦读 资本论', 'isbn': '9787200092882', 'publish_year': 2012},
    {'name': '列宁的一生', 'isbn': '9787501319343', 'publish_year': 2013},
]
ordered_list = sorted(range(len(book_list)), key=lambda k: book_list[k]['publish_year'])
print(ordered_list)  # [0, 2, 3, 1]


# 对象排序
class Book(object):
    def __init__(self, name, isbn, publish_year):
        self.name = name
        self.isbn = isbn
        self.publish_year = publish_year

    def __repr__(self):
        return repr((self.name, self.isbn, self.publish_year))


book_list = [
    Book('北大马克思主义研究', '9787509728529', 2011),
    Book('人的解放', '9787215064003', 2014),
    Book('西方经典悦读 资本论', '9787200092882', 2012),
    Book('列宁的一生', '9787501319343', 2013),
]
# sorted 按出版年降序排序
ordered_list = sorted(book_list, key=lambda book: book.publish_year, reverse=True)
print(
    ordered_list)  # [('人的解放', '9787215064003', 2014), ('列宁的一生', '9787501319343', 2013), ('西方经典悦读 资本论', '9787200092882', 2012), ('北大马克思主义研究', '9787509728529', 2011)]
# sort 按出版年升序排序
book_list.sort(key=lambda book: book.publish_year)
print(
    book_list)  # [('北大马克思主义研究', '9787509728529', 2011), ('西方经典悦读 资本论', '9787200092882', 2012), ('列宁的一生', '9787501319343', 2013), ('人的解放', '9787215064003', 2014)]

# 获取对象排序索引
book_list = [
    Book('北大马克思主义研究', '9787509728529', 2011),
    Book('人的解放', '9787215064003', 2014),
    Book('西方经典悦读 资本论', '9787200092882', 2012),
    Book('列宁的一生', '9787501319343', 2013),
]
ordered_list = sorted(range(len(book_list)), key=lambda k: book_list[k].publish_year)
print(ordered_list)  # [0, 2, 3, 1]
