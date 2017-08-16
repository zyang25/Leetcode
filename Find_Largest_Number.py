class Solution:

	def FindLargestNumber(arr):

		if len(arr) < 0:
			return

		maxEle = arr[0]
		for ele in arr:
			if maxEle < ele:
				maxEle = ele
		return maxEle