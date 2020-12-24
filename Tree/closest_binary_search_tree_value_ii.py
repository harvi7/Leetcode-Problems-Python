class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        res = []
        def inOrder(root):
            if not root: return
            inOrder(root.left)
            if len(res) == k:
                if abs(target - root.val) < abs(target - res[0]): res.pop(0)
                else: return
            
            res.append(root.val)
            inOrder(root.right)
        
        inOrder(root)
        return res