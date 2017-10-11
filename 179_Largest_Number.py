# Given a list of non negative integers, arrange them such that they form the largest number.

# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

# Note: The result may be very large, so you need to return a string instead of an integer.

# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.




arr = [3,30,34,5,9]


maxEle = arr[0]
result = None
for idx, val in enumerate(arr[1:]):
	for idx2, val2 in enumerate(str(val)):
		if val > maxEle:

		
		break