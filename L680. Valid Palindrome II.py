# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.


class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        i, j = 0, len(s) - 1

        while i <= len(s)/2 and j >= len(s)/2:
            left = s[i].lower()
            right = s[j].lower()

            if left != right:
                if not left.isalnum():
                    i += 1
                    continue
                elif not right.isalnum():
                    j -= 1
                    continue
                else:
                    return False
            else:
                i += 1
                j -= 1
        return True

print(Solution().validPalindrome('abca'))