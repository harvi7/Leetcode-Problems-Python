class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None
        prev, curr = None, head
        while curr:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev