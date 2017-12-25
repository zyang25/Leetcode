# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

# Simple solution from others ->
# public class Solution {
#     public boolean hasPathSum(TreeNode root, int sum) {
#         if(root == null)
#             return false;
#         if(root.left == null && root.right == null && root.val == sum)
#             return true;
#         return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val);
#     }
# }


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    @staticmethod
    def print_tree(root):

        if root:
            print('     '+str(root.val))
            TreeNode.print_tree(root.left)
            TreeNode.print_tree(root.right)

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        sum_so_far = 0
        path_stack = []
        if self.path_sum(root, sum, sum_so_far, path_stack):
            return True
        else:
            return False

    def path_sum(self, root, target, sum_so_far, path_stack):

        if not root:
            return None

        sum_so_far += root.val
        path_stack.append(root.val)

        if self.path_sum(root.left, target, sum_so_far, path_stack):
            return True

        if self.path_sum(root.right, target, sum_so_far, path_stack):
            return True
        
        ele = path_stack.pop()
        # leaf
        if root.left == root.right and root.left == None:
            if sum_so_far == target:
                return True
        



#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
t = TreeNode(5)
t.left = TreeNode(4)
t.left.left = TreeNode(11)
t.left.left.right = TreeNode(2)
t.left.left.left = TreeNode(7)

t.right = TreeNode(8)
t.right.left = TreeNode(13)
t.right.right = TreeNode(4)
t.right.right.right = TreeNode(1)

# t = TreeNode(1)
# t.left = TreeNode(2)

# TreeNode.print_tree(t)

print(Solution().hasPathSum(t, 28))