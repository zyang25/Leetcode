# Given an absolute path for a file (Unix-style), simplify it.

# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# //// -> /


class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if path == '':
            return ''

        data = []
        path = path.split('/')
        for l in path[::-1]:
            if l == '..':
                data.append('..')
            elif l != '.' and l!= '':
                data.append(l)
        re = ''
        result = []
        while len(data) > 0:
            ele = data.pop()
            if ele == '..' and len(data) > 0:
                data.pop()
            else:
                result.append(ele)

        if len(result) == 0:
            return '/'
        else:
            for e in result:
                re += '/' + e
        return re

print(Solution().simplifyPath("/"))