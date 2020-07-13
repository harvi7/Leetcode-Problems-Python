class Codec:
    
    def __init__(self):
        self.NULL_SYMBOL= "X"
        self.DELIMITER = ","
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: 
            return self.NULL_SYMBOL + self.DELIMITER

        leftSerialized = self.serialize(root.left)
        rightSerialized = self.serialize(root.right)

        return str(root.val) + self.DELIMITER + str(leftSerialized) + str(rightSerialized)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodesLeftToMaterialize = []
        nodesLeftToMaterialize.extend(data.split(self.DELIMITER))
        return self.deserializeHelper(nodesLeftToMaterialize)
    
    def deserializeHelper(self, nodesLeftToMaterialize):

        valueForNode = nodesLeftToMaterialize.pop(0)

        if valueForNode == self.NULL_SYMBOL:
            return None

        newNode = TreeNode(int(valueForNode))
        newNode.left = self.deserializeHelper(nodesLeftToMaterialize)
        newNode.right = self.deserializeHelper(nodesLeftToMaterialize)

        return newNode