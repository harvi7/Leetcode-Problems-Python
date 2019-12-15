class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res, queue= [], [root] if root else []        
        while queue:
            res.append(queue[0].val)
            cur_level, queue = queue, []
            for child in cur_level:
                if child.right: queue.append(child.right)
                if child.left: queue.append(child.left)
        return res