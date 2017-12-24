# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
# Example:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Restrictions:
# The string consists of lower English letters only.
# Length of the given string and k will in the range [1, 10000]


# break the string into parts and rest
# check every part of string and add to result
# check rest if it's less than k or greater than k

class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        parts = int(len(s) / (2 * k))
        rest = len(s) % (2 * k)
        result = ''
        if parts > 0:
            for i in range(0, parts):
                end = 2 * k * (i + 1)
                start = 2 * k * i
                result += self.reverseStringOfK(s[start:end], k)
        
        end = len(s)
        start = parts * 2 * k
        if rest > k:
            result += self.reverseStringOfK(s[start:end], k)
        else:
            result += self.reverseStringOfK(s[start:end], rest)
        return result


    def reverseStringOfK(self, s, k=None):
        s = list(s)
        mid = int(int(k) / 2)
        for i in range(0, mid):
            temp = s[i]
            s[i] = s[k-i-1]
            s[k-i-1] = temp
        return ''.join(s)

#print(Solution().reverseStringOfK("hello",2))
print(Solution().reverseStr("abcdefg", 2))