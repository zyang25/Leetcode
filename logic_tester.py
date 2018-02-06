'''Write a program to encode a string in below format : 
aabbbcc => a2b3c2
aaa            => a3                                  
aabbaa   => a2b2a2   

abab => a1b1a1b1

ab = > a1b1

'''

def encodeString(s):
    
    if len(s) == 0:
        return None
    if len(s) == 1:
        return s
    
    prev = s[0]
    curr = s[1]
    
    counter = 1
    
    lCounter = 1
    result = ''
    while counter < len(s):
        
        curr = s[counter]
        if prev == curr:
            lCounter += 1
        else:
            result += prev + str(lCounter)
            lCounter = 1
        
        prev = curr
        counter+= 1
        
    return result

# s = "aabbbcc"
# print(encodeString(s))



# class UniqueNumber:
    
#     def __init__(self, arr):
#         self.arr = arr

#     def __iter__(self):
#         self.index = 0
#         dup = set()
#         return self

#     def __next__(self):
#         if self.index == len(self.arr):
#             raise StopIteration
        
#         ele = self.arr[self.index]
#         self.index += 1
#         return ele

# uni = UniqueNumber([1,2,3,4,4,5])

# for ele in uni:
#     print(ele)


class Solution(object):
    def wordBreak(self, s, wordDict):
        def canBreak(s, m, wordDict):
            if s in m: return m[s]
            if s in wordDict: 
                m[s] = True
                return True
            
            for i in range(1, len(s)):
                r = s[i:]
                if r in wordDict and canBreak(s[0:i], m, wordDict):
                    m[s] = True
                    return True
            
            m[s] = False
            return False
            
        return canBreak(s, {}, set(wordDict))

Solution().wordBreak("Ilovesamsung", ['I','love','samsung','sam','sung'])

