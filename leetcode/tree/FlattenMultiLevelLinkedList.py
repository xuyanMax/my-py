class Flatten(object):
    # https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3386/
    def flatten(self, head):
        if not head:
            return
        stack = [head]
        pre = Node(0)
        while stack:
            curr = stack.pop()
            curr.prev = pre
            pre.next = curr
            pre = curr
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None

        head.prev = None
        return head


