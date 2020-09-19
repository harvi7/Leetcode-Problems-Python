class Solution:
    def __init__(self):
        self.memo = {0: [], 1: [TreeNode(0)]}
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N not in self.memo:
            ans = []
            for x in range(N):
                y = N - 1 - x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right
                        ans.append(bns)
            self.memo[N] = ans

        return self.memo[N]