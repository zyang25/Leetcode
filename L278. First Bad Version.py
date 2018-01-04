# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        pass

    def findBad(self, start, end):
        
        if start > end:
            return -1

        mid = start + (end - start) / 2

        # not bad
        if not isBadVersion(mid):
            self.findBad(start, mid)
        else:
            self.findBad(mid-1, end)


        