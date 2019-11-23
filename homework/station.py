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


method = input()
stops = Stack()
num = 1
out = []
flag = True

for m in method:
    if m == 'A':
        out.append(num)
        num += 1
    elif m == 'B':
        if stops.size() == 5:
            flag = False
            break
        stops.push(num)
        num += 1
    elif m == 'C':
        if stops.isEmpty():
            flag = False
            break
        out.append(stops.pop())

if flag == False:
    print("No")
else:
    print("Yes")
    for i in out:
        print(i)
