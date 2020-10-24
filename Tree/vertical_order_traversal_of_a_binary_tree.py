class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        minHd = maxHd = 0
        
        def verticalTraversal(root):
            nonlocal minHd, maxHd
            queue = deque([(root, 0, 0)])

            while queue:
                node, row, column = queue.popleft()

                if node is not None:
                    columnTable[column].append((row, node.val))
                    minHd = min(minHd, column)
                    maxHd = max(maxHd, column)

                    queue.append((node.left, row + 1, column - 1))
                    queue.append((node.right, row + 1, column + 1))

        verticalTraversal(root)
        
        res = []
        for col in range(minHd, maxHd + 1):
            res.append([val for row, val in sorted(columnTable[col])])

        return res