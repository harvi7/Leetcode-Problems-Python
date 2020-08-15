# https://leetcode.com/problems/construct-string-from-binary-tree/discuss/104000/Python-Straightforward-with-Explanation

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t: return ''
        left = '({})'.format(self.tree2str(t.left)) if (t.left or t.right) else ''
        right = '({})'.format(self.tree2str(t.right)) if t.right else ''
        return '{}{}{}'.format(t.val, left, right)