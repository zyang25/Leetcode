
import sys
arr = [1,5,4,3]


print(sys.maxsize)
first = sys.maxsize
second = sys.maxsize



for i in arr:
    if i < first:
        second = first
        first = i
    elif i < second:
        second = i
    
print(second)


import sys

first = -sys.maxsize -1

print(first)