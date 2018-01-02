# Remove all elements from a linked list of integers that have value val.

# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5

# The key for this problem is dummy node point to the link list
# Why dummy? Because there is no definition for previous node so we need to create one

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head:

            if head.val == val:
                prev.next = head.next
                head = prev

            prev = head
            head = head.next

        return dummy.next

ln = ListNode(1)

ln.next = ListNode(2)
ln.next.next = ListNode(6)
ln.next.next.next = ListNode(3)
ln.next.next.next.next = ListNode(4)
ln.next.next.next.next.next = ListNode(5)
ln.next.next.next.next.next.next = ListNode(6)

Solution().removeElements(ln,6)