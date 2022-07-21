# In Python (2.7), implement at least 2 classes implementing
# a cyclic FIFO buffer. Explain the pros and cons of each implementation.

class FIFOqueue():
	len = 0
	items = []

	def __init__(self, items):
		for item in items:
			self.len += 1
			self.push(item)

	def push(self, item):
		self.items = [item] + self.items

	def pop(self):
		item = self.items[self.len]
		self.len -= 1
		self.items = self.items[:self.len+1]

		return item


	def printinfo(self):
		print'Items = ',
		print self.items

fifo = FIFOqueue([1, 2, 3, 4])
fifo.printinfo()

fifo.push(5)
fifo.printinfo()

print'Items.pop() =', fifo.pop()
fifo.printinfo()