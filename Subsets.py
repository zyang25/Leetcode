def get_subset(arr):
    for i in range(0, len(arr)):
        j = i + 1
        while j < len(arr):
            subset = list()

            for e in arr[i:j]:
                subset.append(e)

            print(subset)
            j += 1

get_subset([1,2,3,4,5])