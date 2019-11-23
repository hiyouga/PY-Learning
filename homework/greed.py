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

    def sumnum(self):
        return sum(self._elems)

pocket = Stack()
n = int(input())
while True:
    m = int(input())
    if m == 0:
        break
    if pocket.isEmpty():
        pocket.push(m)
    elif m > pocket.top():
        pocket.pop()
        pocket.push(m)
    else:
        if pocket.size() < n:
            pocket.push(m)

print(pocket.sumnum())
