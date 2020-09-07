class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        height = self.getHeight(root)
        res = [[""] * ((1 << height) - 1) for _ in range(height)]
        self.fill(res,root,0,0,len(res[0]))
        return res
    
    def fill(self, res, root, index, left, right):
        if not root: return 
        mid = (left + right) // 2
        res[index][mid] = str(root.val)
        self.fill(res, root.left, index + 1, left, mid)
        self.fill(res, root.right, index + 1, mid + 1, right)
    
    def getHeight(self, root):
        if not root: return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))