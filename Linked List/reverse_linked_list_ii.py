class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None

        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1

        tail, connection = cur, prev
        while n:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
            n -= 1

        if connection:
            connection.next = prev
        else:
            head = prev
        tail.next = cur
        return head