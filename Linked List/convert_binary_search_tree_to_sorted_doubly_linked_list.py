class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return None
        pre, head = None, None
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left  
            
            root = stack.pop()
            if not pre: 
                head = root  
                
            else:
                pre.right = root
                root.left = pre

            pre = root
            root = root.right

        pre.right = head
        head.left = pre
        return head