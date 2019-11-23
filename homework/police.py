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
def process():
    road = SQueue()
    wait = SQueue()
    n = int(input())
    for i in range(n):
        car = input()
        road.enqueue(car)
    m = int(input())
    for i in range(m):
        car = input()
        wait.enqueue(car)
    command = input()
    for c in command:
        if c == 'A':
            if road.is_empty():
                print("No")
                return
            else:
                road.dequeue()
        elif c == 'B':
            if wait.is_empty():
                print("No")
                return
            else:
                road.enqueue(wait.dequeue())
    while not road.is_empty():
        print(road.dequeue())

process()
