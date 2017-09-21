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
        	print(s[x])

        	if d.get(s[x]) == None:
        		d[s[x]] =1
        	else:
        		d[s[x]] +=1

        
        for x in range(0, len(s)):
            if d.get(s[x]) == 1:
                return x
            
        return -1

print(Solution().firstUniqChar('leetcode'))