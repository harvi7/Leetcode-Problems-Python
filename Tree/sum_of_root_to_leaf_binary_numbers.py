class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        ans = 0
        stack = [(root, 0)]
        while stack:
            node, x = stack.pop()
            x = 2 * x + node.val
            if not node.left and not node.right: 
                ans += x
            else: 
                if node.left : stack.append((node.left , x))
                if node.right: stack.append((node.right, x))
        return ans