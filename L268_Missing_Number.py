class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        newNums = [None] * (len(nums) + 1)

        for x in range(0,len(nums)):
        	newNums[nums[x]] = nums[x]



        for ele in newNums:
        	if ele == None:
        		return newNums.index(ele)

nums = [0,1,3]
print(Solution().missingNumber(nums))