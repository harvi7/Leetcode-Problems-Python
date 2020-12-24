class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = []
        queue.append(root)
        while (queue):
            root = queue.pop(0)
            if (root.right): queue.append(root.right)
            if (root.left): queue.append(root.left)
        return root.val