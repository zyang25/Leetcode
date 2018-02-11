# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s[:]:
            try:
                if c == ')':
                    if stack.pop() != '(':
                        return False
                elif c == ']':
                    if stack.pop() != '[':
                        return False
                elif c == '}':
                    if stack.pop() != '{':
                        return False
                else:
                    stack.append(c)
            except:
                return False

        if len(stack) == 0: 
            return True
        else:
            return False

print(Solution().isValid('['))