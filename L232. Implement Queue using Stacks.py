# Implement the following operations of a queue using stacks.

# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
# Notes:
# You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.st = []
        self.size = 0
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.st.append(x)
        self.size += 1

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.size == 0:
            return None
        
        tempSt = []
        found = None
        for i in range(0, self.size):
            ele = self.st.pop()
            tempSt.append(ele)
        
        for i in range(0, len(tempSt)):
            e = tempSt.pop()

            if i == 0:
                found = e
            else:
                self.st.append(e)
        self.size -= 1
        
        return found
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.size == 0:
            return None
        temSt = []
        found = None
        for i in range(0, self.size):
            e = self.st.pop()
            temSt.append(e)
        
        for i in range(0, len(temSt)):
            e = temSt.pop()
            self.st.append(e)
            if i == 0:
                found = e

        return found
        
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.size == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop())
print(obj.pop())
print(obj.pop())