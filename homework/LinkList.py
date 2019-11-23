class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkList:
    def __init__(self, initdata = []):
        self.root = Node(0)
        self.length = 0
        for d in initdata:
            self.append(d)
    def getLength(self):
        return self.length
    def append(self, d):
        r = self.root
        while not r.next is None:
            r = r.next
        r.next = Node(d)
        self.length += 1
    def insert(self, d, i = 0):
        r = self.root
        if i < self.length:
            while i != 1 and r.next != None:
                r = r.next
                i -= 1
            r.next = Node(d, r.next)
        self.length += 1
    def get(self, i):
        r = self.root
        if i < self.length:
            while i != 0 and r.next != None:
                r = r.next
                i -= 1
            return r.data
        else:
            return -1
    def delete(self, i):
        r = self.root
        if i < self.length:
            while i != 1 and r.next != None:
                r = r.next
                i -= 1
            r.next = r.next.next
        self.length -= 1
    def dump(self):
        r = self.root
        while not r.next is None:
            r = r.next
            print(r.data)

if __name__ == '__main__':
    l = LinkList([5, 4, 3, 2, 1])
    l.insert(7, 3)
    l.insert(8, 3)
    print('Length is', l.getLength())
    print('got', l.get(4))
    l.delete(4)
    l.dump()