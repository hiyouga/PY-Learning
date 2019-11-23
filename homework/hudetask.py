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

n = int(input())
a = SQueue()
b = SQueue()
c = SQueue()
for i in range(n):
    ind, lev = input().split()
    if lev == 'A':
        a.enqueue(ind)
    elif lev == 'B':
        b.enqueue(ind)
    elif lev == 'C':
        c.enqueue(ind)

while not a.is_empty():
    print(a.dequeue())
while not b.is_empty():
    print(b.dequeue())
while not c.is_empty():
    print(c.dequeue())
