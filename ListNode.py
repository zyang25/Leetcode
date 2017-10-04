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
                
	    	temp = temp.next