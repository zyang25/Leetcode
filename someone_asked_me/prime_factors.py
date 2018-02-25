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

        x = 2
        r = []
        mem = dict()
        while x <= n:
            if n % x == 0:
                if mem.get(x) != None or self.isPrime(x):
                    mem[x] = x
                    r.append(x)
                n = n // x
            else:
                x += 1
        return r
    
    def isPrime(self, x):
        for i in range(2,x-1):
            if x % i == 0:
                return False
        return True


print(Solution().countPrimes(5))