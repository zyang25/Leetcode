# 21. Merge Two Sorted Lists


# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import ListNode
class Solution(object):
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		prev = None
		temp = None
		while l1 != None or l2 != None:

			if l1 != None and l2 != None:
				if l1.val > l2.val:
					temp = ListNode(l2.val)
					l2 = l2.next
				else:
					temp = ListNode(l1.val)
					l1 = l1.next

			if l1 == None and l2 != None:
				temp = ListNode(l2.val)
				l2 = l2.next

			if l2 == None and l1 != None:
				temp = ListNode(l1.val)
				l1 = l1.next


			
			
			if prev != None:
				prev.next = temp

			prev = temp

			#temp = temp.next

		return temp

l1 = ListNode(10)
l1.next = ListNode(15)
l1.next.next = ListNode(20)


l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)


result = Solution().mergeTwoLists(l1,l2)

result.pList()