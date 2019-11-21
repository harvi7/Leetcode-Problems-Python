class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        end = False
        queue = [root]
        while queue:
            curr = queue.pop(0)
            if not curr:
                end = True
            else:
                if end:
                    return False
                queue.append(curr.left)
                queue.append(curr.right)
        return True