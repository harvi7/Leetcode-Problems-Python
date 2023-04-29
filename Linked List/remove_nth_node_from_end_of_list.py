class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n <= 0: return head
        
        dummy = ListNode(0)
        dummy.next = head
        preDelete = dummy
        
        for i in range(n):
            if not head:
                return None
            head = head.next
        
        while head:
            preDelete = preDelete.next
            head = head.next
        
        preDelete.next = preDelete.next.next
        
        return dummy.next