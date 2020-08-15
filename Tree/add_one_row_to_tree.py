class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            return TreeNode(v,root)
        queue, depth = [root], 1
        while depth < d - 1:
            temp   = []
            for node in queue:
                if node.left : temp.append(node.left)
                if node.right: temp.append(node.right)
            queue = temp
            depth += 1
            
        for node in queue:
            node.left, node.right = TreeNode(v, node.left, None), TreeNode(v, None, node.right)
            
        return root