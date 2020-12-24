class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        return self.dfs(root, None, 0)
    
    def dfs(self, p, parent, length):
        if not p: return length
        length = length + 1 if (parent and p.val == parent.val + 1) else 1
        return max(length, max(self.dfs(p.left, p, length), self.dfs(p.right, p, length)))