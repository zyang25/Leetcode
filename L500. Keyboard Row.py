# 500. Keyboard Row
# DescriptionHintsSubmissionsDiscussSolution
# DiscussPick One
# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


# American keyboard


# Example 1:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]


class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        d = {
          'Q':0, 'W':0, 'E':0, 'R':0, 'T':0, 'Y':0, 'U':0, 'I':0, 'O':0, 'P':0,
          'A':1, 'S':1, 'D':1, 'F':1, 'G':1, 'H':1, 'J':1, 'K':1, 'L':1,
          'Z':2, 'X':2, 'C':2, 'V':2, 'B':2, 'N':2, 'M':2}

        result = []
        for word in words:
            if len(word) > 0:
                flag = 0
                i = 1
                first = d.get(word[0].upper())
                while i < len(word):
                    if first != d.get(word[i].upper()):
                        flag = 1
                    i += 1

                if flag == 0:
                    result.append(word)


        return result