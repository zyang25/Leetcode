# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Assume that:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
# Complexity:

# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

A = [-1,-3]


def Solution(arr):
    d = {}
    max_num = arr[0]
    min_num = arr[0]
    not_show = False

    for ele in arr:
        if ele > max_num:
            max_num = ele
        
        if ele < min_num:
            min_num = ele
        
        d[ele] = 1

    min_num_in_not_show = max_num
    for x in range(min_num, max_num+1):
        curr = d.get(x)
        if curr is None:
            if x < min_num_in_not_show:
                min_num_in_not_show = x
            not_show = True
    
    if not_show != True:
        return max_num + 1
    elif min_num_in_not_show < 0:
        return 1
    else:
        return min_num_in_not_show

print(Solution(A))

