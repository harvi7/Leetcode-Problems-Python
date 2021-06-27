class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res

        q = [root]
        while q:
            oneLevel = []
            size = len(q)
            for i in range(size):
                n = q.pop(0)
                oneLevel.append(n.val)
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
                    
            res.append(oneLevel)
        return res[::-1]
    
        