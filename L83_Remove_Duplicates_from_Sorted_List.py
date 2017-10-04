# Given a sorted linked list, delete all duplicates such that each element appear only once.

# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def p(self):
    	print(str(self.val))

    def pList(self):


    	temp = self
    	while temp != None:
	    	if temp.next == None:
	    		print(str(temp.val) + '->' + 'None')
	    	else:
	    		print(str(temp.val) + '->' + str(temp.next.val))
	    	print(self.next.val)
	    	temp = self.next
	    	print(temp)

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = head
        while head != None:
        	#print('Begins')
        	
        	temp = head.next

        	if head.next == None or head.next.val != head.val:
        		#prev.next = head
        		#prev = head
        		prev.next = head
        		prev = head
        		prev.pList()
        		

        	
        	head = temp

        return prev



linkedList = ListNode(10)
linkedList.next = ListNode(4)
linkedList.next.next = ListNode(3)


#Solution().deleteDuplicates(linkedList)



linkedList.pList()

