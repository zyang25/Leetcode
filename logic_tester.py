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

s = "aabbbcc"
print(encodeString(s))
        
    
    