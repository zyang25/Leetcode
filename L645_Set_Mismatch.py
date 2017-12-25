# The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]

class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        d = {}
        dup_num = None
        missing_num = None
        for n in nums:
            if d.get(n):
                d[n] += 1
                if d.get(n) == 2:
                    dup_num = n
            else:
                d[n] = 1

        for i in range(1, len(nums)+1):
            if d.get(i) == None:
                missing_num = i
        return [dup_num, missing_num]

print(Solution().findErrorNums([3,2,4,1,5,6,5]))