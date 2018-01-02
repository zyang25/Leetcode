# You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

# The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

# Example 1:
# Input: Binary tree: [1,2,3,4]
#        1
#      /   \
#     2     3
#    /    
#   4     

# Output: "1(2(4))(3)"

# Explanation: Originallay it needs to be "1(2(4)())(3()())", 
# but you need to omit all the unnecessary empty parenthesis pairs. 
# And it will be "1(2(4))(3)".
# Example 2:
# Input: Binary tree: [1,2,3,null,4]
#        1
#      /   \
#     2     3
#      \  
#       4 

# Output: "1(2()(4))(3)"

# Explanation: Almost the same as the first example, 
# except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
from TreeNode import TreeNode


# Think of root + left + right pattern
# Construct something in recursive func without using temp var we need to use return 

# return current node val +                     (left tree)                +                    (right tree)
#                           (current node val + (left tree) + (right tree))  (current node val + (left tree) + (right tree))
class Solution:

    def tree2str(self, t):

        if t == None:
            return ""

        elif t.left == None and t.right == None:
            return t.val + ""
        
        # Special condiction - we don't need right tree if it's none, omit ()
        elif t.right == None:
            return t.val + '(' + self.tree2str(t.left) + ')'

        return t.val + '(' + self.tree2str(t.left) + ')(' + self.tree2str(t.right) + ')'

#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1


t = TreeNode()


Solution().tree2str(t.t1())