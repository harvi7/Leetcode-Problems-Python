class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.generate(1, n) if n else []

    def generate(self, low, high):
        if low > high:
            return [None]
        ans = []

        for i in range(low, high + 1):
            leftSubtrees = self.generate(low, i - 1)
            rightSubtrees = self.generate(i + 1, high)
            for leftSubtree in leftSubtrees:
                for rightSubtree in rightSubtrees:
                    root = TreeNode(i)
                    root.left  = leftSubtree
                    root.right = rightSubtree
                    ans.append(root)
        return ans