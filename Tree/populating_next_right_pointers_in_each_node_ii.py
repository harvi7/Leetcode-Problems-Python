class Solution:
    def connect(self, root: 'Node') -> 'Node':
        parent = root
        childHead, child = None, None
        while parent:
            while parent:
                if parent.left:
                    if not childHead:
                        childHead = parent.left
                    else:
                        child.next = parent.left
                    child = parent.left
                    
                if parent.right:
                    if not childHead:
                        childHead = parent.right
                    else:
                        child.next = parent.right
                    child = parent.right
                parent = parent.next
            parent = childHead
            childHead, child = None, None
        return root