class addBinary(object):
    def sol(self, strA, strB):
        a = list(strA)
        b = list(strB)
        result = ''
        carry = 0
        while a or b or carry:
            if a:
                carry+=int(a.pop())
            if b:
                carry+=int(b.pop())
            result += str(carry % 2)
            carry = carry / 2
        return result[::-1]
