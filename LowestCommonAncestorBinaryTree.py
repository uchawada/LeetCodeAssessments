## NOT WORKING
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        
        
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        print(self.build_tree_from_list(root))
        
    
    def build_tree_from_list(self, values):
        if root_node is None:
            return None
        if root == p or root == q:
            return root
        
        # Search for p and q in the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are not None, this root is the LCA
        if left and right:
            return root
        
        # If one of the sides returned a node, that means p or q was found there
        return left if left else right




