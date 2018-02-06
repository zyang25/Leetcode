# Consider the following dictionary 
# { i, like, sam, sung, samsung, mobile, ice, 
#   cream, icecream, man, go, mango}

# Input: "ilikesamsungmobile"
# Output: i like sam sung mobile
#         i like samsung mobile

# Input: "ilikeicecreamandmango"
# Output: i like ice cream and man go
#         i like ice cream and mango
#         i like icecream and man go
#         i like icecream and mango

# tup = {"mobile","samsung","sam","sung","man","mango","icecream","and","go","i","love","ice","cream"}

# def word_exist(word):
#     for i in tup:
#         if i == word:
#             return True
#     return False

# def can_break(s, r):
    
#     if len(s) == 0: res.append(r[1:])

#     for i in range(1, len(s)):
#         prefix = s[0:i+1]
        
#         if word_exist(prefix):
#             print('prefix '+prefix)
#             print('rp ' + r + prefix)
#             can_break(s[i:], r + prefix)
# res = list()
# can_break("ilovesamsung", r = '')



# class Solution:
#     # @param s, a string
#     # @param dict, a set of string
#     # @return a list of strings
#     def check(self, s, dict):
#         dp = [False for i in range(len(s)+1)]
#         dp[0] = True
#         for i in range(1, len(s)+1):
#             for k in range(0, i):
#                 if dp[k] and s[k:i] in dict:
#                     dp[i] = True
#         return dp[len(s)]
        
#     def dfs(self, s, dict, stringlist):
#         #if self.check(s, dict):
#         if len(s) == 0:
#             Solution.res.append(stringlist[1:])
#         for i in range(1, len(s)+1):
#             if s[:i] in dict:
#                 self.dfs(s[i:], dict, stringlist+' '+s[:i])
    
#     def wordBreak(self, s, dict):
#         Solution.res = []
#         self.dfs(s, dict, '')
#         return Solution.res

# Solution().wordBreak('ilovesamsung', ["mobile","samsung","sam","sung","man","mango","icecream","and","go","i","love","ice","cream"])

d = ["mobile","samsung","sam","sung","man","mango","icecream","and","go","i","love","ice","cream"]
res = []

def word_exist(w):
    if w in d:
        return True
    return False


def word_break_dfs(s, string_list):

    if len(s) == 0:
        res.append(string_list[1:])

    for i in range(1, len(s) + 1):
        prefix = s[:i]
        if word_exist(prefix):
            rest_string = s[i:]
            word_break_dfs(rest_string, string_list + ' ' + prefix)

def word_break(s):
    word_break_dfs(s, '')

word_break('ilovesamsung')

print(res)



def wordBreak(self, s, wordDict):
    if not s:
        return []
    n = len(s)
    dp = [[] for x in range(n + 1)]
    dp[0] = [0]
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i].append(j)
    
    res = []
    self.backTracking(dp, s, n, res, '')
    return res

wordBreak('ilovesamsung', ["mobile","samsung","sam","sung","man","mango","icecream","and","go","i","love","ice","cream"])





