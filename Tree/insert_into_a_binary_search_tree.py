class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None: 
            return TreeNode(val)
        currNode = root
        while True:
            if currNode.val <= val:
                if currNode.right:
                    currNode = currNode.right
                else: 
                    currNode.right = TreeNode(val)
                    break             
            else:
                if currNode.left:
                    currNode = currNode.left
                else:
                    currNode.left = TreeNode(val)
                    break
        return root