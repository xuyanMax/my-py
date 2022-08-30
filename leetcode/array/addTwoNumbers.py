class AddTwoNumbers:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


instance = AddTwoNumbers()
list1 = ListNode(2)
pt1 = list1
pt1.next = ListNode(4)
pt1 = pt1.next
pt1.next = ListNode(3)

list2 = ListNode(5)
pt2 = list2
pt2.next = ListNode(6)
pt2 = pt2.next
pt2.next = ListNode(4)

list = instance.addTwoNumbers(list1, list2)

while list:
    print(list.val)
    list = list.next

