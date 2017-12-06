# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
import sys
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.d = list()
        self.min_stack = list()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.d.append(x)
        if len(self.min_stack) == 0 or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.top() == self.getMin():
            self.min_stack.pop()
            return self.d.pop()
        return self.d.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.d[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
    
    def getAllMinStack(self):
        return [e for e in self.min_stack]
    
    def getAllStack(self):
        return [e for e in self.d]


ms = MinStack()
ms.push(7)
ms.push(4)
ms.push(5)
ms.push(1)
print(ms.getAllStack())

print(ms.getMin())
ms.pop()
ms.pop()
print(ms.getMin())
print(ms.getAllStack())

