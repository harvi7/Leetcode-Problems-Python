class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result = []
        if not root: return result
        q = []
        q.append(root)
        levelSum = 0
        while q:
            levelSum = 0
            size = len(q)
            for _ in range(size):
                currNode = q.pop(0)
                levelSum += currNode.val
                if currNode.left: q.append(currNode.left)
                if currNode.right: q.append(currNode.right)
            levelAvg = levelSum / size
            result.append(levelAvg)
        return result