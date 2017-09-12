# Write a function that takes a string as input and returns the string reversed.

# Example:
# Given s = "hello", return "olleh".


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        result = ""
        for x in range(length-1,-1,-1):
        	result += s[x]
        return result


print Solution().reverseString("hello")