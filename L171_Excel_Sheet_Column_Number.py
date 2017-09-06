# Related to question Excel Sheet Column Title

# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 



class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        result = 0
        for c in reversed(s):
        	dec = ord(c) - 64
        	print dec
        	if count == 0:
        		result += dec
        	else:
        		# 10 -> 26
        		result += dec * 26 ** count

        	count += 1



        return result

        

print Solution().titleToNumber('AAA')