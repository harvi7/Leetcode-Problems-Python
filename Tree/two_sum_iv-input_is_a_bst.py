class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False

        return self.helper(root, set(), k)
    
    def helper(self, node, nodes, k):
        if not node:
            return False

        if k - node.val in nodes: return True
        nodes.add(node.val)
        return self.helper(node.left, nodes, k) or self.helper(node.right, nodes, k)