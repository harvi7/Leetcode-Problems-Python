class Solution:
    prev = None
    max_count = 0
    current_count = 0 
    result = []
    
    def findMode(self, root: TreeNode) -> List[int]:    
        self.traverse(root)       
        return self.result
    
    def traverse(self, node):
        if not node: return
        self.traverse(node.left)

        if self.prev == node.val: self.current_count += 1
        else: self.current_count = 1
       
        if self.current_count > self.max_count: 
            self.result = [node.val]
            self.max_count = self.current_count
        elif self.current_count == self.max_count:
            self.result.append(node.val)
     
        self.prev = node.val      
        self.traverse(node.right)