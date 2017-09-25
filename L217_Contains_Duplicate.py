# Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
        	return false

        d = {}
        for ele in nums:
        	if d.get(ele) == None:
        		d[ele] = 1
        	else:
        		d[ele] += 1

        	if d[ele] >= 2:
        		return True
        return False


print(Solution().containsDuplicate([0]))