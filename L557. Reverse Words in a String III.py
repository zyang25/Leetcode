# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_s = list(s)
        for i in range(0, len(s)/2):
            temp = s[i]
            new_s[i] = s[len(s)-i-1]
            new_s[len(s)-i-1] = temp
        return ''.join(new_s)

print(Solution().reverseWords('Hello'))
