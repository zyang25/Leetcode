'''
Write a program to encode a string in below format : 

aabbbcc => a2b3c2
aaa            => a3                                  
aabbaa   => a2b2a2   

abab => a1b1a1b1

ab = > a1b1

'''

# You need to watch out the last index, otherwise the last character group will be added

def encodeString(s):
    
    if len(s) == 0:
        return ''
    if len(s) == 1:
        return s + str(1)
    
    prev = s[0]
    curr = s[1]
    
    counter = 1
    
    lCounter = 1
    result = ''
    while counter < len(s):
        
        # start from second c
        curr = s[counter]
        
        # last character
        if prev == curr and counter == len(s)-1:
            result += prev + str(lCounter+1)
        elif prev == curr:
            lCounter += 1
        else:
            result += prev + str(lCounter)
            lCounter = 1
        
        prev = curr
        counter+= 1
        
    return result

s = "aabbbcc"
print(encodeString(s))