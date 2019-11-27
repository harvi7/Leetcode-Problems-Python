class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        paths = []
        self.find_paths(root, sum, [], paths)
        return paths
    
    def find_paths(self, root, sum, ls, paths):
        if not root.left and not root.right and sum == root.val:
            ls.append(root.val)
            paths.append(ls)
        if root.left:
            self.find_paths(root.left, sum-root.val, ls+[root.val], paths)
        if root.right:
            self.find_paths(root.right, sum-root.val, ls+[root.val], paths)