# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

# You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

# Example 1:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
# Example 2:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
# Note:
# The length of both lists will be in the range of [1, 1000].
# The length of strings in both lists will be in the range of [1, 30].
# The index is starting from 0 to the list length minus 1.
# No duplicates in both lists.


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = {}

        # Updated Algorithm
        for x in range(0,len(list1)):
        	if x not in d:
        		d[list1[x]] = 1
        	else:
        		d[list1[x]] +=1

        posSum = len(list1) + len(list2) - 2
        result = []
        for key in list2:
        	if d.get(key) == 1:
        		indexSum = list1.index(key) + list2.index(key)
        		if indexSum < posSum:
        			posSum = indexSum
        			# We need to reset the list because there is smaller index
        			result = []
        			result.append(key)
        		elif indexSum == posSum:
        			result.append(key)



        return result

arr1 = ["Shogun","Tapioca Express","Burger King","KFC"]
arr2 = ["KFC","Shogun","Burger King"]




print(Solution().findRestaurant(arr1,arr2))