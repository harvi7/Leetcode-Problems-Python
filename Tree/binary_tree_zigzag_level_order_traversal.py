class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        deque1 = collections.deque()
        deque2 = collections.deque()
        if root:
            deque1.append(root)
        res, l = [], []
        while deque1 or deque2:
            while deque1:
                n = deque1.pop()
                l.append(n.val)
                if n.left: deque2.append(n.left)
                if n.right: deque2.append(n.right)
            if l:
                res.append(l)
            l = []
            while deque2:
                n = deque2.pop()
                l.append(n.val)
                if n.right: deque1.append(n.right)
                if n.left: deque1.append(n.left)           
            if l:
                res.append(l)
            l = []
        return res