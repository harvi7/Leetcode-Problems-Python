class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if root.val == key:
            root = self.delete(root, key)
        elif (root.val < key):
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root
    
    def delete(self, root, key):
        if not root.left and not root.right:
            return None
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        helper = root.right
        while helper.left:
            helper = helper.left
        helper.left = root.left
        return root.right