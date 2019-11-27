class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        tail = head
        length = 1
        while ( tail.next ):
            tail = tail.next
            length += 1         
        if k == 0:
            return head
        else :
            k %= length
        steps_to_new_head = length - k
        tail.next = head
        new_tail = tail
        while steps_to_new_head > 0:
            new_tail = new_tail.next
            steps_to_new_head -= 1
        
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head