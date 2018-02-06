# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output:  321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 123 -> 321
        #left_rest = x / 10
        #most_right = x % 10
        new_num = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        while x != 0:
            # 123 -> 3
            most_right = x % 10

            # 3 | 3 * 10 + 2 = 32 | 32 * 10 + 1 = 321
            new_num = new_num * 10 + most_right

            # 123 -> 12
            x = x // 10
        if new_num > 2147483647:
            return 0
        else:
            return sign * new_num

print(Solution().reverse(-123))

#print(Solution().reverse(-123))


# from collections import Counter
# from collections import OrderedDict

# class LeagueTable:
#     def __init__(self, players):
#         self.standings = OrderedDict([(player, Counter()) for player in players])
       
#     def record_result(self, player, score):
#         self.standings[player]['games_played'] += 1
#         self.standings[player]['score'] += score

#     def sorted_key(p):
#         print(p)

#     def player_rank(self, rank):
#         #print(self.standings)
#         new_d = sorted(self.standings, key=lambda p: (-self.standings[p]['score'], -self.standings[p]['games_played']))
#         return new_d[rank-1]
      
# table = LeagueTable(['Charles', 'Marcus', 'Mike', 'Chris', 'Arnold', ])
# table.record_result('Charles', 2)
# table.record_result('Marcus', 1)
# table.record_result('Mike', 2)
# table.record_result('Mike', 3)
# table.record_result('Arnold', 5)
# table.record_result('Chris', 5)
# print(table.player_rank(2))
