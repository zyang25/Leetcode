# Given a binary tree, return all root-to-leaf paths.

# For example, given the following binary tree:

#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:

# ["1->2->5", "1->3"]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import TreeNode


class Solution:

    def __init__(self, *args, **kwargs):
        self.paths = list()

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        path = []
        self.get_path(root, str(root.val))

    def get_path(self, root, path):
        
        if not root:
            return

        if not root.left and not root.right:
            self.paths.append(path)
		
        if root.left:
        	self.get_path(root.left, path + '->' + str(root.left.val))

        if root.right:
            self.get_path(root.right, path + '->' + str(root.right.val))

t = TreeNode()
t1 = t.t1()
TreeNode.print_tree(t1)
Solution().binaryTreePaths(t1)
