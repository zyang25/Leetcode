
# -*- coding: utf-8 -*-
# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

# Note:
# The given integer is guaranteed to fit within the range of a 32-bit signed integer.
# You could assume no leading zero bit in the integer’s binary representation.
# Example 1:
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
# Example 2:
# Input: 1


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # int(str, base=2)
        int(''.join(str((1 - int(x))) for x in bin(num)[2:]), 2)

Solution().findComplement(5)