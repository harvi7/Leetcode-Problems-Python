class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root: return ans
        self.level(root, ans)
        return ans
    
    def level(self, root, ans):
        if not root: return -1
        curr_height = max(self.level(root.left, ans), self.level(root.right, ans)) + 1
        if len(ans) <= curr_height:
            ans.append([])
        ans[curr_height].append(root.val)
        return curr_height