def Binary_Search(arr, l, r, target):

	#Find the middle index
	mid = l + (r - l)/2

	#Loop for every section
	if l <= r:
		
		if arr[mid] == target:
			return target
		elif arr[mid] < target:
			return Binary_Search(arr, l, mid - 1, target)
		else:
			return Binary_Search(arr, mid + 1, r, target) 
	else:
		return -1

arr = [10,-12,34,11,3,4,5,3,1,3,4]

print Binary_Search(arr, 0, len(arr)-1, 55)