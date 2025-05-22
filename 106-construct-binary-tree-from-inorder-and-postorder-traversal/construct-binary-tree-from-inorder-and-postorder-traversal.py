class Solution(object):
    def buildTree(self, inorder, postorder):
        if not postorder:
            return None
        v = postorder[-1]
        root = TreeNode(val=v)
        i = inorder.index(v)
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i + 1 :], postorder[i:-1])
        return root
        