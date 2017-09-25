# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = list()

        d = {}
        for ele in nums:
        	if d.get(ele) == None:
        		d[ele] = 1
        	else:
        		d[ele] += 1
        print(d)

        for key,value in d.items():
        	if value > len(nums)/2:
        		return key


nums = [2,3,4,2,2,2,2,2,2]
print(Solution().majorityElement(nums))