class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pointer = dummy
        while pointer:
            node = pointer
            i = 0
            while i < k and node:
                node = node.next
                i += 1
            
            if not node: break
            
            curr = pointer.next
            prev = None
            for i in range(k):
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            
            tail = pointer.next
            tail.next = curr
            pointer.next = prev
            pointer = tail

        return dummy.next