class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def helper1(root, s):
            if not root: return
            helper1(root.left, s)
            s.append(root.val)
            helper1(root.right, s)
    
        def helper2(root, s):
            if not root: return
            helper2(root.left, s)
            root.val = s.pop()
            helper2(root.right, s)

        s1, s2 = [], []
        helper1(root, s1)

        while s1:
            if not s2:
                s2.append(s1.pop())
            else:
                s2.append(s2[-1] + s1.pop())
                
        helper2(root, s2)
        return root