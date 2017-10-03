# Reverse a singly linked list.

# click to show more hints.

# Hint:
# A linked list can be reversed either iteratively or recursively. Could you implement both?




# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def p(self):
    	print(str(self.val))

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev = None
        while head != None:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
            break
        return prev



linkedList = ListNode(10)
linkedList.next = ListNode(15)
linkedList.next.next = ListNode(3)



print(Solution().reverseList(linkedList))