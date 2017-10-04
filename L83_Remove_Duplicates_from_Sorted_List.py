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

        while curr != None:
        	#print('Begins')
        	
        	temp = head.next

            if curr.val != prev.val:
                prev.next = curr
                prev = curr

            curr = curr.next

        return prev



linkedList = ListNode(10)
linkedList.next = ListNode(4)
linkedList.next.next = ListNode(3)


#Solution().deleteDuplicates(linkedList)



linkedList.pList()

