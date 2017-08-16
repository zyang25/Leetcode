class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        result = x ^ y
        count = 0
        for i in '{0:b}'.format(result):
        	if i == '1':
        		count = count + 1
        return count


s = Solution()
s.hammingDistance(1,2)