class Solution:
    def rob(self, root: TreeNode) -> int:
        def robSub(root):
            if not root:
                return [0] * 2

            left = robSub(root.left)
            right = robSub(root.right)
            result = [0] * 2

            result[0] = max(left[0], left[1]) + max(right[0], right[1])
            result[1] = root.val + left[0] + right[0]

            return result
            
        result = robSub(root)
        return max(result[0], result[1])