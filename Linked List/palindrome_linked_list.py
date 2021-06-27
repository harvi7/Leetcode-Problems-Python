class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next: return True
        s = []
        slow, fast = head, head
        while fast and fast.next:
            s.append(slow.val)
            slow = slow.next
            fast = fast.next.next
            
        if fast: 
            slow = slow.next
        while slow:
            if s.pop() != slow.val: return False
            slow = slow.next
        return True