# Given two arrays, write a function to compute their intersection.

# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

# Note:
# Each element in the result must be unique.
# The result can be in any order.



class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = set()

        for x in nums1:
        	for y in nums2:
        		if x == y:
        			result.add(x)
        return list(result)


print Solution().intersection(list(range(1,10,2)), list(range(1,10,1)))