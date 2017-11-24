# Two for loop to swap the numbers

# The first loop to take the element in order
# the second loop to take the sub array of the first element

def BubbleSort(arr):

	x = 0
	while x < len(arr):
		y = x + 1
		while y < len(arr):
			if arr[y] < arr[x]:
				temp = arr[y]
				arr[y] = arr[x]
				arr[x] = temp
			y += 1
		x += 1
	return arr

arr = [10, 33, 21, 1, 2, 7]
print(BubbleSort(arr))
