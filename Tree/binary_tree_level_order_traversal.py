class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        queue = deque([root,])
        while queue:
            oneLevel = []
            size = len(queue)         
            for i in range(size):
                node = queue.popleft()
                oneLevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(oneLevel)
        return res