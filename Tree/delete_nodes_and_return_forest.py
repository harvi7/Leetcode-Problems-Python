class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        res = []
        
        def removeNodes(node, is_root):
            if not node: return None
            toDelete = node.val in to_delete_set
            if is_root and not toDelete:
                res.append(node)
            node.left = removeNodes(node.left, toDelete)
            node.right = removeNodes(node.right, toDelete)
            return None if toDelete else node
        
        removeNodes(root, True)
        return res