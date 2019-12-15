class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack, res = [], []       
        if not root: return res
        
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            for child in node.children[::-1]:
                stack.append(child)
        return res