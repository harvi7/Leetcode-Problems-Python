class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root: return 0
        if root.val > R: return self.rangeSumBST(root.left, L, R)
        if root.val < L: return self.rangeSumBST(root.right, L, R)
        return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)