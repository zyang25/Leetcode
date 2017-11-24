# -*- coding: utf-8 -*-
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 231.

# Example:

# Input: x = 1, y = 4

# Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑

# The above arrows point to positions where the corresponding bits are different.


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        # Get all the difference of two numbers
        res = x ^ y
        c = 0

        # Get result's binary format
        # 0bXXX
        # count how many 1
        for i in bin(res):
            if i == '1':
                c += 1
        return c

Solution().hammingDistance(3,4)