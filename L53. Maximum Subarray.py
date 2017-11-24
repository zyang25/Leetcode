# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

# click to show more practice.

# More practice:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # largest_subset_left, largest_subset_right = 0,0
        # largest_sum = nums[0]
        # # Start index
        # for i in range(0, len(nums)):
        #     j = i
        #     # End index
        #     while j < len(nums):
        #         sum_of_subset = 0
        #         test = list()
        #         for e in nums[i:j+1]:
        #             test.append(e)
        #             sum_of_subset += e
        #         #sum_of_subset = str(sum(nums[i:j]))    
        #         print('sum is {1}, Subset is {0}, i,j {2},{3}'.format(test, str(sum(nums[i:j])), str(i), str(j) ))
        #         if sum_of_subset > largest_sum:
        #             largest_sum = sum_of_subset
        #             largest_subset_left, largest_subset_right = i, j
        #             #print('The largest subset is {0}'.format(largest_subset))
        #             #print(nums[i:j])
        #         j += 1
        # return largest_sum
        max_sum = -2147483649
        curr_sum = 0
        for n in nums:
            
            if curr_sum < 0:
                curr_sum = n
            else:
                curr_sum += n

            max_sum = max(max_sum, curr_sum)

        return max_sum

print(Solution().maxSubArray([-1,2]))

                