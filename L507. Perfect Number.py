# We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

# Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
# Example:
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# Note: The input number n will not exceed 100,000,000. (1e8)

from math import math
class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0 or num == 1:
            return False
        r = []
        x = 1
        # find all divisors
        while x <  math.sqrt(num):
            if num % x == 0:
                r.append(x)
        print(r)

Solution().checkPerfectNumber(num)