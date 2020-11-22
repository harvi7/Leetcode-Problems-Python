class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        dict = {}
        for i in range(len(inorder)):
            dict[inorder[i]] = i
        return self.helper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, dict)
    
    def helper(self, preorder, pLeft, pRight, inorder, iLeft, iRight, dict):
        if pLeft > pRight or iLeft > iRight: return None
        i = dict[preorder[pLeft]]
        cur = TreeNode(preorder[pLeft])
        cur.left = self.helper(preorder, pLeft + 1, pLeft + i + iLeft, inorder, iLeft, i - 1, dict)
        cur.right = self.helper(preorder, pLeft + i - iLeft + 1, pRight, inorder, i + 1, iRight, dict)
        return cur