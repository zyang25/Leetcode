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




def test():
    stack = []
    def test2():
        for i in range(12):
            stack.append(i)
        return stack

    print(test2())
    stack = []
    print(test2())

def test_tree():
    from TreeNode import TreeNode
    import Queue
    t = TreeNode().t1()
    q = Queue.LifoQueue()
    q.put(t)
    def traverse(tree):

#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
        while not q.empty():
            node = q.get()
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)

        # if tree == None:
        #     return
        # else:
        #     print(tree.val)
        #     traverse(tree.left)
        #     traverse(tree.right)
    
    traverse(t)

test_tree()


#print([i for i in range(100)])


def f(*args, **kwargs):
    print(args, kwargs)
d = {'a':7,'b':8,'c':9}

f(1,2,3,4,c=321)


class MyClass(object):
    
    def __init__(self):
        self._some_property = "properties are nice"
        self._some_other_property = "VERY nice"
    
    def normal_method(*args,**kwargs):
        print("calling normal_method({0},{1})".format(args,kwargs))
    
    @classmethod
    def class_method(*args,**kwargs):
        print("calling class_method({0},{1})".format(args,kwargs))
    
    @staticmethod
    def static_method(*args,**kwargs):
        print("calling static_method({0},{1})".format(args,kwargs))
    
    @property
    def some_property(self,*args,**kwargs):
        print("calling some_property getter({0},{1},{2})".format(self,args,kwargs))
        return self._some_property
    
    @some_property.setter
    def some_property(self,*args,**kwargs):
        print("calling some_property setter({0},{1},{2})".format(self,args,kwargs))
        self._some_property = args[0]
    
    @property
    def some_other_property(self,*args,**kwargs):
        print("calling some_other_property getter({0},{1},{2})".format(self,args,kwargs))
        return self._some_other_property
    