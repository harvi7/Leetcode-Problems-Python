# https://leetcode.com/problems/boundary-of-binary-tree/discuss/508274/python-preorder-traversal

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root: return

        left_boundary, right_boundary, leaves = [], [], []
        self.helper(root, 0, left_boundary, right_boundary, leaves)
        return left_boundary + leaves + right_boundary[::-1]

    def helper(self, root, flag, left_boundary, right_boundary, leaves):
        def isLeaf(cur):
            return not cur.left and not cur.right
        
        if not root: return
        
        if isLeaf(root):
            leaves.append(root.val)
            return

        if flag == 0:
            left_boundary.append(root.val)
            self.helper(root.left, 1, left_boundary, right_boundary, leaves)
            self.helper(root.right, 2, left_boundary, right_boundary, leaves)
        elif flag == 1:
            left_boundary.append(root.val)
            if root.left:
                self.helper(root.left, 1, left_boundary, right_boundary, leaves)
                self.helper(root.right, 3, left_boundary, right_boundary, leaves)
            else:
                self.helper(root.right, 1, left_boundary, right_boundary, leaves)
        elif flag == 2:
            right_boundary.append(root.val)
            if root.right:
                self.helper(root.left, 3, left_boundary, right_boundary, leaves)
                self.helper(root.right, 2, left_boundary, right_boundary, leaves)
            else:
                self.helper(root.left, 2, left_boundary, right_boundary, leaves)
        else:
            self.helper(root.left, 3, left_boundary, right_boundary, leaves)
            self.helper(root.right, 3, left_boundary, right_boundary, leaves)