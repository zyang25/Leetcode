# find the time spot that most users online

arrival = [1, 2, 10, 5, 5]
offline = [4, 5, 12, 9, 12]


# 1     2
#        3      4
#               4       6
#                5              10


def most_user(arr, off):
    arr = sorted(arr)
    off = sorted(off)
    print(arr)
    print(off)

    c = 1
    i, j = 1, 0
    max_users = 0
    time = 0
    while i < len(arr) and j < len(off):
        
        if arr[i] <= off[j]:
            c += 1
            if c > max_users:
                max_users = c
                time = arr[i]
            i+=1
        else:
            c-=1
            j+=1

    return max_users, time

print(most_user(arrival, offline))
