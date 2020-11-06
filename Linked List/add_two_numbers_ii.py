class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next

        while l2:
            s2.append(l2.val)
            l2 = l2.next
            
        tot_sum = 0
        res = ListNode(0)
        while s1 or s2:
            if s1:
                tot_sum += s1.pop()
            if s2:
                tot_sum += s2.pop()
            res.val = tot_sum % 10
            head = ListNode(tot_sum // 10)
            head.next = res
            res = head
            tot_sum //= 10

        return res.next if res.val == 0 else res