class queue:
    def __init__(self):
        self.item = ['Saurabh', 'michael', 'ninanaxcvx']

    def nqueue(self, item):
        q = [item]
        self.item = q + self.item
        return (self.item)

    def dqueue(self):
        return (self.item.pop(0))

    def front(self):
        return (self.item(0))

    def size(self):
        return (len(self.item))


q = queue()
q.nqueue('chocolate')
print(q.dqueue())


q.pop()