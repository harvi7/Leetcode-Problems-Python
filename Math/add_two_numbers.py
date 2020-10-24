class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        p, q, curr = l1, l2, dummyHead
        carry = 0
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            out  = carry + x + y
            carry = out // 10;
            curr.next = ListNode(out % 10)
            curr = curr.next
            if p: p = p.next
            if q: q = q.next
        if carry > 0: 
            curr.next = ListNode(carry)
        return dummyHead.next