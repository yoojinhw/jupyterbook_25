from DataStructureCode.ListNode import *

class CircularLinkedList:
	def __init__(self):
		self.tail = ListNode("dummy", None)
		self.tail.next = self.tail
		self.numItems = 0

	def insert(self, i:int, data) -> None:
		if (i >= 0 and i <= self.numItems):
			prev = self.getNode(i - 1)
			newNode = ListNode(data, prev.next)
			prev.next = newNode
			if i == self.numItems:
				self.tail = newNode
			self.numItems += 1
		else:
			print("index", i, ": out of bound in insert()")

	def append(self, data) -> None:
		newNode = ListNode(data, self.tail.next)
		self.tail.next = newNode
		self.tail = newNode
		self.numItems += 1

	def pop(self, i:int):
		if self.isEmpty():
			return None
		if i == -1:
			i = self.numItems - 1
		if (i >= 0 and i <= self.numItems - 1):
			prev = self.getNode(i - 1)
			retItem = prev.next.data
			prev.next = prev.next.next
			if i == self.numItems - 1:	
				self.tail = prev		  
			self.numItems -= 1
			return retItem
		else:
			return None

	def remove(self, x):
		(prev, curr) = self.findNode(x)
		if curr != None:
			prev.next = curr.next
			if curr == self.tail:	 
				self.tail = prev	  
			self.numItems -= 1
			return x
		else:
			return None

	def get(self, i):
		if self.isEmpty():
			return None
		if i == -1:
			i = self.numItems - 1
		if (i >= 0 and i <= self.numItems - 1):
			return self.getNode(i).data
		else:
			return None

	def index(self, x) -> int:
		cnt = 0
		for element in self:
			if element == x:
				return cnt
			cnt += 1
		return -12345

	def isEmpty(self) -> bool:
		return self.numItems == 0

	def size(self) -> int:
		return self.numItems

	def clear(self):
		self.tail = ListNode("dummy", None)
		self.tail.next = self.tail
		self.numItems = 0

	def count(self, x) -> int:
		cnt = 0
		for element in self:
			if element == x:
					cnt += 1
		return cnt

	def extend(self, a):
		for x in a:
			self.append(x)
 
	def copy(self) -> b'CircularLinkedList':
		a = CircularLinkedList()
		for element in self:
			a.append(element)
		return a

	def reverse(self) -> None:
		head = self.tail.next
		prev = head; curr = prev.next; next = curr.next
		curr.next = head; head.next = self.tail; self.tail = curr
		for i in range(self.numItems - 1):
			prev = curr; curr = next; next = next.next
			curr.next = prev

	def sort(self) -> None:
		a = []
		for element in self:
			a.append(element)
		a.sort() 
		self.clear()
		for element in a:
			self.append(element)

	def findNode(self, x) -> (ListNode, ListNode):
		head = prev = self.tail.next
		curr = prev.next
		while curr != head:
			if curr.data == x:
				return (prev, curr)
			else:
				prev = curr; curr = curr.next
		return (None, None)
 
	def getNode(self, i:int) -> ListNode:
		curr = self.tail.next
		for index in range(i+1):
			curr = curr.next
		return curr

	def printList(self):
		curr = self.tail.next
		curr = curr.next
		while curr.data != "dummy":
			print(curr.data, end = ' ')
			curr = curr.next
		print()

