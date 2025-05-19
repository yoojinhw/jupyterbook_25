class ListQueue:
	def __init__(self):
		self.queue = []

	def enqueue(self, x): # insert an element to the end of the queue
		self.queue.append(x)

	def dequeue(self): # remove an element from the front of the queue
		return self.queue.pop(0) 

	def front(self): # returns the front node of the queue without deleting it
		if self.isEmpty():
			return None
		else:
			return self.queue[0]

	def isEmpty(self) -> bool: # returns true if queue is empty, else false.
		return (len(self.queue) == 0);
 
	def dequeueAll(self): # clean the queue
		self.queue.clear()

	def size(self): # length of the queue
		return len(self.queue)

	def printQueue(self): # print elements from front to end
		print("Elements from front to end: ")
		for i in range(len(self.queue)):
			print(self.queue[i], end = ' ')

