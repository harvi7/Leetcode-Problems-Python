class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.num, self.index = 0, 0
        inorder(self, root, k)
        return self.num
    
def inorder(self, root, k):
    if not root: return
    inorder(self, root.left, k)
    self.index += 1
    if self.index == k: 
        self.num = root.val
        return
    inorder(self, root.right, k)