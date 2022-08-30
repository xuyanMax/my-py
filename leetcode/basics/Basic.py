class Basic(object):
    ##读入整数
    a = int(input())
    print(a)
    print(type(a))

    name = input()
    # 格式化输出
    print('I am {} and I am studying Python in Nowcoder!'.format(name))
    print('I am %s and I am studying Python in Nowcoder!' % name)
    # print函数控制小数的位数，
    num = float(input())
    print('%.2f' % num)

    # 类型转换
    num = float(int(input()))
    print(num)
    print(type(num))

    # 十六进制数字的大小
    num = input()
    print(int(num, 16))  # 默认base=10

    l = len(num)
    res = 0
    power = pow(16, l - 1)
    str = '0123456789ABCDEF'
    for i in range(l):
        num1 = num[i]
        res += str[num1] * power
        power /= 16

    print(int(res))

    ##join two strings
    a = "num"
    b = "string"
    print(a + b)
    print("".join([a, b]))
