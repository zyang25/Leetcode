# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# Notes:
# You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.


class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_arr = str.split(' ')
        pat_arr = list(pattern)

        if len(str_arr) != len(pat_arr):
            return False

        c = 0
        d = {}
        d2 = {}
        for e in pattern:
            pattern_val = d.get(e)
            d2_val = d2.get(str_arr[c])
            if pattern_val != None:
                if pattern_val != str_arr[c]:
                    return False
            elif d2_val != None and d2_val != e:
                return False
            else:
                d[e] = str_arr[c]
                d2[str_arr[c]] = e

            c += 1
        print(d)
        return True

# pattern = "abba"
# string = "dog cat cat dog"

pattern = "abba"
string = "dog dog dog dog"

print(Solution().wordPattern(pattern, string))
