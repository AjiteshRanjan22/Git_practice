class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self, newNode):
		if self.head == None:
			self.head = newNode
		else:
			#john ben mathew 
			lastNode = self.head
			while True:
				if lastNode.next is None:
					lastNode.next = newNode
					break
				lastNode = lastNode.next

	def printlist(self):
		if self.head == None:
			print('List is empty')

		currentNode = self.head
		while True:
			print(currentNode.data,end=' ')
			if currentNode.next is None:
				break
			currentNode = currentNode.next
firstNode = Node('John')
linkedlist = LinkedList()
linkedlist.insert(firstNode)
secondNode = Node('Ben')
linkedlist.insert(secondNode)
thirdNode = Node('Mathew')
linkedlist.insert(thirdNode)
fourthNode = Node('Ajitesh')
linkedlist.insert(fourthNode)
fifthNode = Node('Ben')
linkedlist.insert(fifthNode)
sixthNode = Node('John')
linkedlist.insert(sixthNode)
seventhNode = Node('Mathew')
linkedlist.insert(seventhNode)
eightnode = Node('Pushpa')
linkedlist.insert(eightnode)
# linkedlist.removeDuplicate(firstNode)
linkedlist.printlist()