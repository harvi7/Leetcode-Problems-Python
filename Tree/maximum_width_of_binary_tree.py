class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        max_width = 0;
        deq = deque()
        deq.append((root, 1)) 
        
        while deq:
            qlength = len(deq)
            firstIndex = deq[0][1]
            while qlength > 0:
                node, lastIndex = deq.popleft()
                if node.left: deq.append((node.left, 2 * lastIndex))
                if node.right: deq.append((node.right, 2 * lastIndex + 1))
                qlength -= 1
            max_width = max(max_width, lastIndex - firstIndex + 1); 
        return max_width  