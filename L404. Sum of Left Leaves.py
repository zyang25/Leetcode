# Find the sum of all left leaves in a given binary tree.

# Example:

#     3
#    / \
#   9  20
#     /  \
#    15   7

# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

from TreeNode import TreeNode

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        
        if root.left == None and root.right == None:
            count = root.val
            return count
        else:
            count = 0

        if root.left:
            count += self.sumOfLeftLeaves(root.left)
        
        if root.right:
            count += self.sumOfLeftLeaves(root.right.left)

        # why we need to return count here
        # because when the right node is traversed, and it's not the leave
        # it will just end the program return nothing which is None type
        # so the stack will take the none type go back to the parent
        # at this point, None + count will throw exception
        # we can think that after right node traverse, we always need to return something to parent
        return count

        

        

t = TreeNode()
tree = t.t1()

                #        5
                #       / \
                #      4   8
                #     /   / \
                #    11  13  4
                #   /  \      \
                #  7    2      1



print(Solution().sumOfLeftLeaves(tree))




        