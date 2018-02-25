# Description:

# Count the number of prime numbers less than a non-negative number, n.

# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        # 12
        # 2 -> 2 6
        #     r = []
        #     x = 2

        if n < 2:
            return 0
        
        # set all number to be prime number
        # validate the non prime number
        r = [1] * (n + 1)
        r[0], r[1], r[2] = 0, 0, 1
        for i in range(2, n + 1):
            # if it's prime number, find all the number and set it to false
            if r[i]:
                j = i
                p = i * j
                while p < n:
                    r[p] = 0
                    p = i * j
                    j += 1
        r[2] = 0
        return sum(r)


print(Solution().countPrimes(5))