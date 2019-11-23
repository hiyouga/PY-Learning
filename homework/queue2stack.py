class SQueue(object):
	def __init__(self, init_len=8):
		self.__elem = [0] * init_len
		self.__len = init_len
		self.__head = 0
		self.__num = 0


	def __extend(self):
		old_len = self.__len
		self.__len *= 2
		new_elems = [0] * self.__len
		for i in range(old_len):
			new_elems[i] = self.__elem[(self.__head + i) % old_len]
		self.__elem, self.__head = new_elems, 0


	def is_empty(self):
		return self.__num == 0


	def peek(self):
		if self.__num == 0:
			raise QueueUnderflow
		return self.__elem[self.__head]
		

	def enqueue(self, e):
		if self.__num == self.__len:
			self.__extend()
		self.__elem[(self.__head + self.__num) % self.__len] = e
		self.__num += 1
		
		
	def dequeue(self):
		if self.__num == 0:
			raise QueueUnderflow
		e = self.__elem[self.__head]
		self.__head = (self.__head + 1) % self.__len
		self.__num -= 1
		return e

class Qtack():
    def __init__(self):
        self.__elem = SQueue()
        self.__back = SQueue()
        self.__len = 0
    def is_empty(self):
        return self.__len == 0
    def push(self, e):
        while not self.__elem.is_empty():
            self.__back.enqueue(self.__elem.dequeue())
        self.__elem.enqueue(e)
        self.__len += 1
        while not self.__back.is_empty():
            self.__elem.enqueue(self.__back.dequeue())
    def pop(self):
        if self.__len == 0:
            raise StackUnderflow
        self.__len -= 1
        return self.__elem.dequeue()

def process():   
    n = int(input())
    qtk = Qtack()
    out = []
    remain = []
    for i in range(n):
        num = input()
        qtk.push(num)
    m = int(input())
    for i in range(m):
        cin = input().split()
        if cin[0] == 'A':
            qtk.push(cin[1])
        elif cin[0] == 'B':
            if qtk.is_empty():
                print('No')
                return
            else:
                out.append(qtk.pop())
    while not qtk.is_empty():
        remain.append(qtk.pop())
    print(' '.join(out))
    print(' '.join(remain))

process()
