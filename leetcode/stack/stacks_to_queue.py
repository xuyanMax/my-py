class stacks_to_queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def peek(self):
        while not self.s2:
            while not self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def pop(self):
        self.peek()
        return self.s2.pop()

    def empty(self):
        return not self.s1 and not self.s2
