class Stack:
    def __init__(self):
        self._elems = []

    def isEmpty(self):
        return self._elems == []

    def top(self):
        if self._elems == []:
            raise Exception('Stack is empty when using top()!')
        else:
            return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems == []:
            raise Exception('Stack is empty when doing pop()!')
        else:
            return self._elems.pop()

    def size(self):
        return len(self._elems)

m, n = map(int, input().split())
out = Stack()
mapping = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

while m > 0:
    out.push(mapping[m % n])
    m //= n

seq = []
while not out.isEmpty():
    seq.append(out.pop())

print(''.join(seq))
