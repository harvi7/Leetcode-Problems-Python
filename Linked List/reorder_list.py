class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: 
            return
        
        l1, slow, fast, prev = head, head, head, None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        l2 = self.reverse(slow)
        
        self.merge(l1, l2)
    
    def reverse(self, head):
        prev = None
        curr = head
        nextNode = None
        
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev
    
    def merge(self, l1, l2):
        while l1:
            l1Next, l2Next = l1.next, l2.next
            l1.next = l2
            
            if l1Next is None:
                break
            l2.next = l1Next
            l1 = l1Next
            l2 = l2Next