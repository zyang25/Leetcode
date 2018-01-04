# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# Example:

# Input: "Hello World"
# Output: 5


# If the first character is space, continue
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 0:
            return 0
        
        arr = list(s)
        
        count = 0
        spaceFlag = False
        for c in arr[::-1]:
            
            if c == ' ' and count == 0:
                continue
            elif c == ' ':
                return count
                count = 0
            else:
                count += 1
        
        return count
