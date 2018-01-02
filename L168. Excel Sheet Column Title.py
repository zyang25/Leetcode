# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

# For example:

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
# Credits:
# Special thanks to @ifanchu for adding this problem and creating all test cases.

# every letter represent 26 digit

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        