def simplify(path):
    res = ''
    data = []
    ele_arr = path.split('/')
    for e in ele_arr:
        if e != ' ':
            if e != '.':
                data.append(e)
            # if e == '..':
            #     res = '/' + data.pop()
    count = 0
    for e in data:
        if e == '..':
            res = '/' + data.pop()
        else:

            res += '/' + e
    return res
    
print(simplify('/ac/./ba'))
print(simplify('/ac/../ba'))