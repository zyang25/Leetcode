# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Order the string by character
        
        logicSet = set()


        for x in s:
        	if x not in logicSet:
        		logicSet.add(x)
        	

        # if len(s) == 1:
        # 	return 0

        # for x in range(0,len(s)-1):
        # 	found = 0
        # 	print 'x loop - ', x

        # 	for y in range(x+1,len(s)):
        # 		print 'y loop - ', y
        # 		if s[x] == s[y]:
        # 			print 'found ', s[x], s[y]
        # 			found = 1
        # 			break
        	
        # 	if found == 0:
        # 		return x

        # return -1



print Solution().firstUniqChar('aadadaad')