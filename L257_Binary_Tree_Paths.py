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
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

	arr = []
	path = ''
	def addToPath(self, val, lastEle = False):
		
		if lastEle == False:
			path += str(val) + '->'
		else:
			path += str(val)

		return path

	def binaryTreePaths(self, root):
		"""
        :type root: TreeNode
        :rtype: List[str]
        """
		if root == None:
			addToPath(root.val, True)
			arr.append(path)
			return
		
		if root.left == None:
			addToPath(root.val)
			binaryTreePaths(root.right)
		if root.right == None:
			addToPath(root.val)
			binaryTreePaths(root.left)





tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)

tree.left.right = TreeNode(5)

print(Solution().binaryTreePaths(tree).arr)       