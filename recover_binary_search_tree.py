class Solution:    
    def __init__(self):
        self.first, self.second, self.prev = None, None,  None
        
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if self.prev and self.prev.val > root.val:
            if not self.first:
                self.first = self.prev
            self.second = root
        self.prev = root
        self.inorder(root.right)