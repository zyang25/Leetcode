# Given an absolute path for a file (Unix-style), simplify it.

# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# //// -> /


# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".


class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        s = ''
        index = 0
        
        # add eof to the string can pass all the scenarios
        path += '/'
        
        for c in path:
            if c != '/':
                s += c
            elif c == '/':
                if s == '..':
                    if len(stack)>0:
                        stack.pop()
                elif s != '.' and s != '':
                    stack.append(s)
                s = ''
            index += 1

        p = ''
        for e in stack:
            p += '/' + e
        
        if p == '':
            p = '/'

        return p

print(Solution().simplifyPath("/home/../etc/./var/abc///da"))
print(Solution().simplifyPath("///eHx/.."))