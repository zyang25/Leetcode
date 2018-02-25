

s = 'aabbcc'
def compressedString(s):
    
    if s == '':
        return ''
    
    if len(s) == 1:
        return s
    
    prev = s[0]
    curr = s[1]
    
    lCounter = 1
    counter = 1
    result = ''
    while counter < len(s):
        
        curr = s[counter]
        # abc
        # last character
        if prev == curr and counter == len(s) - 1:
            result += prev + str(lCounter + 1)
        elif prev == curr:
            lCounter += 1
        else:
            if lCounter > 1:
                result += prev + str(lCounter)
            else:
                result += prev
            lCounter = 1
        
        prev = curr
        counter += 1
    
    print(result)
    return result

compressedString(s)