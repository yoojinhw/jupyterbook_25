class ListStack:
	def __init__(self):
		self.stack = []

	def push(self, x):
		self.stack.append(x)

	def pop(self):
		return self.stack.pop()

	def top(self):
		if self.isEmpty():
			return None
		else:
			return self.stack[-1]

	def isEmpty(self) -> bool:
		return len(self.stack) == 0

	def size(self):
  		return len(self.stack)

	def printStack(self):
		print("Elements from top to bottom: ")
		for i in range(len(self.stack)-1, -1, -1):
			print(self.stack[i], end = ' ')
		print()

