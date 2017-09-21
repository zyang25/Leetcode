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
        d = {}

        for x in range(0, len(s)):
        	print s[x]

        	if d.get(s[x]) == None:
        		d[s[x]] =1
        	else:
        		d[s[x]] +=1

        print d.items()
        for key, value in d.items():
        	if value == 1:
				return s.index(key)        		


        return -1

print Solution().firstUniqChar('leetcode');