# The count-and-say sequence is the sequence of integers with the first five terms as following:

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth term of the count-and-say sequence.

# Note: Each term of the sequence of integers will be represented as a string.

# When we deal with string counting, it's really hard to count characters
# So we can add a dummy element such as * at the end of the string
# we only compare the current one with the previous one
# then we will not need to deal with the last character scenario

class Solution:

    def countString(self, s):
        s_arr = list(s)
        # dummy element
        s_arr.append('*')
        i = 1
        c = 1
        last_c = s_arr[0]
        r = ''
        while i < len(s_arr):

            # if the current one equals to the last one
            if last_c == s_arr[i]:
                c += 1
            else:
                r += str(c) + last_c
                c = 1
            last_c = s_arr[i]
            i += 1
        return r

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"

        if n == 2:
            return "11"

        return self.countString(self.countAndSay(n-1))



print(Solution().countAndSay(5))
        

        
