class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]      
        levelSum = 0
        while queue:
            levelSum = 0
            for i in range(len(queue)):
                currentNode = queue.pop(0)
                levelSum += currentNode.val
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
        return  levelSum