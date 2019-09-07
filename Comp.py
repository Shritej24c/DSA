class Arraystack:
    def __init__(self):
        # create a stack
        self.stack = []

    def push(self, item):
        return self.stack.append(item)

    def length(self):
        return len(self.stack)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[len(self.stack)-1]

    def isEmpty(self):
        return self.stack == 0

    def __print__(self):
        print(self.stack)




C = Arraystack()

