# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.

# Think about the last word. How are you going to do it
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word = ''
        result = ''
        count = 0
        for c in s:
            
            
            # this is a word
            if c == ' ':
                reWord = self.reverseWord(word)
                result += reWord
                result += ' '
                word = ''
            else:
                word += c
            

            if count == len(s) - 1 and len(word) > 0:
                result += self.reverseWord(word)

            count += 1

        return result

    def reverseWord(self, w):
        arr = list(w)
        mid = len(arr) / 2
        i = 0
        while i < mid:
            temp = arr[i]
            arr[i] = arr[len(arr)-1-i]
            arr[len(arr)-1-i] = temp
            i += 1
        return ''.join(arr)
#print(Solution().reverseWord("Let's"))
print(Solution().reverseWords('I love anna liang'))