from DataStructureCode.ListNode import *


class SimpleLinkedList:
	def __init__(self):
		self.head = ListNode(data="dummy", nextNode=None)
		self.numItems = 0

	def append(self, data):
		prev = self.getNode(self.numItems-1)
		newNode = ListNode(data, prev.next)
		prev.next = newNode
		self.numItems += 1

	def insert(self, i:int, data):
  		if i >= 0 and i <= self.numItems:
    			prev = self.getNode(i - 1)
    			newNode = ListNode(data, prev.next)
    			prev.next = newNode
    			self.numItems += 1
  		else:
    			print("index", i, ": out of bound in insert()") 

	def pop(self, i:int):
		if (i >= 0 and i <= self.numItems-1):
			prev = self.getNode(i - 1)
			curr = prev.next
			prev.next = curr.next
			retItem = curr.data
			self.numItems -= 1
			return retItem
		else:
			return None

	def remove(self, x):
  		i = self.index(x)
  		if i != None:
    			prev = self.getNode(i - 1)
    			curr = prev.next
    			prev.next = curr.next  
    			self.numItems -= 1
  		else:
    			return None

	def getNode(self, i:int) -> ListNode:
		curr = self.head
		for index in range(i+1):
			curr = curr.next
		return curr

	def get(self, i:int):
		if self.isEmpty():
			return None
		if (i >= 0 and i <= self.numItems - 1):
			return self.getNode(i).data
		else:
			return None

	def printList(self):
		curr = self.head.next
		while curr != None:
			print(curr.data, end = ' ')
			curr = curr.next
		print()

	def extend(self, a:'SimpleLinkedList'):
		for index in range(a.size()):
			self.append(a.get(index))
 
	def copy(self):
		a = SimpleLinkedList()
		for index in range(self.numItems):
			a.append(self.get(index))
		return a

	def reverse(self):
		a = SimpleLinkedList()
		for index in range(self.numItems):
			a.insert(0, self.get(index))
		self.clear()
		for index in range(a.size()):
			self.append(a.get(index))

	def index(self, x):
		curr = self.head.next
		for index in range(self.numItems):
			if curr.data == x:
				return index
			else:
				curr = curr.next
		return None

	def isEmpty(self) -> bool:
		return self.numItems == 0

	def size(self) -> int:
		return self.numItems

	def clear(self):
		self.head = ListNode("dummy", None)
		self.numItems = 0

	def count(self, x) -> int:
		cnt = 0
		curr = self.head.next 
		while curr != None:
			if curr.data == x:
					cnt += 1
			curr = curr.next
		return cnt
	

# a = SimpleLinkedList()
# a.append(1); a.append(3); a.append(5); a.append(7); a.append(11)
# a.printList()
# a.insert(4,9)
# a.size()
# a.isEmpty()
# a.index(3)
# a.pop(1)
# a.printList()
# a.remove(9)
# a.printList()