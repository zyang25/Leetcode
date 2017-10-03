# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

# Note:
# You may assume that both strings contain only lowercase letters.

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true




class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = {}
        for ele in magazine:

        	if d.get(ele) == None:
        		d[ele] = 1
        	else:
        		d[ele] += 1

        for ele in ransomNote:
        	if d.get(ele) == None:
        		return False



        return True


print(Solution().canConstruct('aa','ab'))