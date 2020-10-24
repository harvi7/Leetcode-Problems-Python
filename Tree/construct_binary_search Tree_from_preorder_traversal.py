class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        n = len(preorder)
        if not n: return None
        
        root = TreeNode(preorder[0])         
        stack = [root, ] 
        
        for i in range(1, n):
            node, child = stack[-1], TreeNode(preorder[i])
            
            while stack and stack[-1].val < child.val: 
                node = stack.pop()
                
            if node.val < child.val:
                node.right = child 
            else:
                node.left = child 
            stack.append(child)
  
        return root