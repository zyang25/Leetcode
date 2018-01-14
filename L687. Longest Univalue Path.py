# Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

# Note: The length of path between two nodes is represented by the number of edges between them.

# Example 1:

# Input:

#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output:

# 2
# Example 2:

# Input:

#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output:

# 2


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from TreeNode import TreeNode

class Solution:

    max_num = 0

    def longestUnivaluePath(self, root):
        self.longestPath(root, None)
        return self.max_num
    
    def longestPath(self, root, prev):

        if not root:
            return 0

        if prev != None and root.val == prev.val:
            count = 1
        else:
            count = 0
        
        count += self.longestPath(root.left, root)
        count += self.longestPath(root.right, root)

        # this is the entry point when we interated through all the route and back to the root

        if root != prev:
            if count > self.max_num:
                self.max_num = count
            count = 0
           
        return count

t = TreeNode()
tree = t.get_same_nodes_tree()

print(Solution().longestUnivaluePath(tree))


