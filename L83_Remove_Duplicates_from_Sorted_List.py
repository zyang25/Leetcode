# Given a sorted linked list, delete all duplicates such that each element appear only once.

# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

from ListNode import ListNode

class Solution(object):
	def deleteDuplicates(self, head):
		"""
        :type head: ListNode
        :rtype: ListNode
        """
		curr = head
		prev = head

		newHead = prev

		while curr != None:

			if curr.val != prev.val:
				prev.next = curr
				prev = curr
			elif curr.next == None:
				prev.next = None
			curr = curr.next

		return newHead



linkedList = ListNode(10)
linkedList.next = ListNode(4)
linkedList.next.next = ListNode(3)


Solution().deleteDuplicates(linkedList).pList()



#linkedList.pList()

