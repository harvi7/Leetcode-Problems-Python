class BSTIterator:
    
    def leftMostInorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left
    
    def __init__(self, root: TreeNode):
        self.stack = list()
        self.leftMostInorder(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        self.leftMostInorder(node.right)
        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return not len(self.stack) == 0 