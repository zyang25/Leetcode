# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

# Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

	def __init__(self):
		self.val = None
		self.next = None
		self.val = 10
		self.next = ListNode(20)
		self.next.next = ListNode(5)
		pass

	def deleteNode(self, node):
		"""
		:type node: ListNode
		:rtype: void Do not return anything, modify node in-place instead.
		"""

		if node == None:
			return

		nodeFound = None
		while self != None:

			# if nodeFound != None:
			# 	self = nodeFound
			# 	nodeFound = None
			# 	break

			if node.val == self.val:
				print('Found it' + str(self.val))
				self = self.next
				print('Current node', self.val)
				break

			print('Current node', self.val)

			self = self.next



nodes = ListNode(20)


Solution().deleteNode(nodes)