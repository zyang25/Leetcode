# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.


# Deduction
# two arrays are sorted, and num1 has enough space to be merged
# [1,3,5,7] [0,2,4,6]
# two iterator go through num1 and num2
# if num1 < num2, shift elements one place and insert

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j = m -1, n -1
        it = m + n - 1

        while i >= 0 and j >= 0:
            if nums2[j] > nums1[i]:
                nums1[it] = nums2[j]
                j -= 1
                it -= 1
            else:
                nums1[it] = nums1[i]
                i -= 1
                it -= 1
        while j >= 0:
            nums1[it] = nums2[j]
            j -= 1
            it -= 1
        while i >=0:
            nums1[it] = nums1[i]
            i -= 1
            it -= 1

        print(nums1)

nums1 = [0]
nums2 = [1]

Solution().merge(nums1, 0, nums2, 1)