# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        

        # I - 1, V - 5, X - 10, L - 50, C - 100

        

        d = {'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        result = 0
        x = 0
        while x < len(s):

        	if s[x] == 'I':
        		if x+1 < len(s) and d.get(s[x+1]) != None:
        			result += d.get(s[x+1]) - 1
        			x += 2
        		else:
        			result += 1
        	else:
        		result += d.get(s[x])

        	x += 1
        
        return result





print(Solution().romanToInt('DCXXI'))