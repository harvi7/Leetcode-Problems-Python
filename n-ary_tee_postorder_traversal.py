class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack, res = [], []

        if not root: return res
     
        stack.append(root)
        while stack: 
            node = stack.pop()
            res.insert(0, node.val)
            for child in node.children: 
                stack.append(child)
        return res