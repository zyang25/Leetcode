'''
Design a dictionary class which can set all values in O(1)
'''

class SpecialDictionary(object):
    '''
    Default values solution
    '''
    def __init__(self, *args, **kwargs):
        self._default = 0
        self.d = {}

    def set_value(self, k, v):
        self.d[k] = v
    
    def set_all(self, v):
        self.d = {}
        self._default = v

    def get(self, k):
        if self.d.get(k):
            return self.d[k]
        else:
            return self._default
    
    def print_all(self):
        for k, v in self.d.items():
            print(k,v)

d = SpecialDictionary()
d.set_value('A',12)
d.set_value('B',13)
d.set_value('C',2)

d.set_all(1000)
d.set_value('D',17)
d.print_all()

class SpecialDictionary2(object):
    '''
    Default values solution
    '''
    def __init__(self, *args, **kwargs):
        self._default = 0
        self.d = {}
        self.d_shadow = {}

    def set_value(self, k, v):
        self.d[k] = v
    
    def set_all(self, v):
        self.d = {}
        self._default = v

    def get(self, k):
        if self.d.get(k):
            return self.d[k]
        else:
            return self._default
    
    def print_all(self):
        for k, v in self.d.items():
            print(k,v)




