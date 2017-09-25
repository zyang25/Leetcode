# Given two strings s and t, write a function to determine if t is an anagram of s.

# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.

# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
        	return False

        data = s + t
        d = {}
        count = 0
        for ele in data:

        	if count < len(s):
	        	if d.get(ele) == None:
	        		d[ele] = 1
	        	else:
	        		d[ele] += 1

	        	
	        else:
	        	print(d)
        		if d.get(ele) != None:
        			d[ele]= d[ele] - 1
        			if d[ele] == 0:
        				del d[ele]


        	count += 1

       	print(d)

        if len(d) == 0:
        	return True
        else:
        	return False




s1 = 'aacc'
s2 = 'ccac'

print(Solution().isAnagram(s1, s2))
