class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        if not root: return paths
        self.dfs(root, "", paths)
        return paths
    
    def dfs(self, root, path, paths):
        path = path + str(root.val)
        if not root.left and not root.right:
            paths.append(path)
            return
        if root.left: self.dfs(root.left, path + "->", paths)
        if root.right: self.dfs(root.right, path+ "->", paths)