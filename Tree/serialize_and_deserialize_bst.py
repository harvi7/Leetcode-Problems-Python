class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root: return ''
        q = collections.deque([root])
        res = []
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                res.append(str(node.val))
            else:
                res.append('X')
        return ' '.join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data: return None
        data_q = collections.deque(data.split(' '))
        root = TreeNode(int(data_q.popleft()))
        tree_q = collections.deque([root])
        while tree_q:
            node = tree_q.popleft()
            left = data_q.popleft()
            right = data_q.popleft()
            if left != 'X':
                left_node = TreeNode(int(left))
                node.left = left_node
                tree_q.append(left_node)
            if right != 'X':
                right_node = TreeNode(int(right))
                node.right = right_node
                tree_q.append(right_node)
        return root
