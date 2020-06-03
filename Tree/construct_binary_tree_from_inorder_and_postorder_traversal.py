class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inStart, inEnd, postStart, postEnd = 0, len(inorder) - 1, 0, len(postorder) - 1
        return self.helper(inorder, inStart, inEnd, postorder, postStart, postEnd)
    
    def helper(self, inorder, inStart, inEnd, postorder, postStart, postEnd):
        if inStart > inEnd or postStart > postEnd:
            return None

        rootValue = postorder[postEnd]
        root = TreeNode(rootValue)

        k = 0
        for i in range(len(inorder)):
            if (inorder[i] == rootValue):
                k = i
                break
        root.left = self.helper(inorder, inStart, k - 1, postorder, postStart, postStart + k - (inStart + 1))
        root.right = self.helper(inorder, k + 1, inEnd, postorder, postStart + k- inStart, postEnd - 1)

        return root