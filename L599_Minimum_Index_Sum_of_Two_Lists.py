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
        
        lenList1 = len(list1)
        lenList2 = len(list2)
        d = {} 

        for i in range(0,lenList2):


        	if i < lenList1:

        		key1 = list1[i]
        		key2 = list2[i]

        		if key1 not in d: 
        			d[key1] = 1
        		else:
        			d[key1] +=1

        		if key2 not in d:
        			d[key2] = 1
        		else:
        			d[key2] +=1
        		
        		pass
        	else:
        		key2 = list2[i]
        		if key2 not in d:
        			d[key2] = 1
        		else:
        			d[key2] +=1

        leastIndex = lenList1 + lenList2 - 2
        flag = -1
        for key, value in d.items():
        	if value == 2:
        		index1 = list1.index(key)
        		index2 = list2.index(key)
        		if (index1 + index2) <= leastIndex:
        			flag = index1

        print(flag)


        return d
arr1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
arr2 = ["KFC", "Shogun", "Burger King"]




print(Solution().findRestaurant(arr1,arr2))