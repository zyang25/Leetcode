# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from TreeNode import TreeNode
class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cnt = 0
        min_depth = 0
        self.minDepthCounter(root, cnt, min_depth)

    def minDepthCounter(self, root, cnt, min_depth):
        
        if root == None:
            return
        cnt += 1

        self.minDepthCounter(root.left, cnt, min_depth)
        self.minDepthCounter(root.right, cnt, min_depth)

        # leaf
        if root.left == root.right and root.left == None:
            if cnt < min_depth:
                min_depth = cnt
                cnt = 0




#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
t1 = TreeNode().t1()
TreeNode.print_tree(t1)
        