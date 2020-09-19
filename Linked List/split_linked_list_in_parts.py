class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        cur, N = root, 0
        while cur:
            cur = cur.next
            N += 1
        width, remainder = divmod(N, k)

        ans = []
        cur = root
        for i in range(k):
            head = cur
            for j in range(width + (i < remainder) - 1):
                if cur: cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            ans.append(head)
        return ans