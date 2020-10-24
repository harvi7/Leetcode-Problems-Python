# https://leetcode.com/problems/plus-one-linked-list/discuss/676303/Very-easy-to-understand-fast-python-bottom-up-recursive-solution.

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def helper(head):
            if not head.next:
                carry, head.val = divmod(1 + head.val, 10)
                return carry
            carry = helper(head.next)
            carry, head.val = divmod(carry + head.val, 10)
            return carry
        
        sentinel = ListNode(1, head)
        if helper(head): return sentinel
        return head