# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def print_tree(root):
        if root:
            print('     '+str(root.val))
            TreeNode.print_tree(root.left)
            TreeNode.print_tree(root.right)


#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
    
    def t1(self):

        '''
                       5
                      / \
                     4   8
                    /   / \
                   11  13  4
                  /  \      \
                 7    2      1
        '''
        t = TreeNode(5)
        t.left = TreeNode(4)
        t.left.left = TreeNode(11)
        t.left.left.right = TreeNode(2)
        t.left.left.left = TreeNode(7)

        t.right = TreeNode(8)
        t.right.left = TreeNode(13)
        t.right.right = TreeNode(4)
        t.right.right.right = TreeNode(1)
        return t