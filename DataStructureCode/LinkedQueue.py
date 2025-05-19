from DataStructureCode.CircularLinkedList import *

class LinkedQueue:
	
	def __init__(self):
		 self.queue = CircularLinkedList()
	def enqueue(self, x):
		self.queue.append(x)

	def dequeue(self):
		 return self.queue.pop(0)

	def front(self):
		 return self.queue.get(0)

	def isEmpty(self) -> bool:
		 return self.queue.isEmpty()

	def dequeueAll(self):
		 self.queue.clear()

	def size(self):
		 return self.queue.size()

	def printQueue(self):
		print("Elements from front to end: ")
		for i in range(self.queue.size()):
			print(self.queue.get(i), end = ' ')
		print()