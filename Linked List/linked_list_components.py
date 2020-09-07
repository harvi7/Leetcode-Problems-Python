class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        Gset = set(G)
        cur = head
        ans = 0
        while cur:
            if cur.val in Gset and (not cur.next or cur.next.val not in Gset):
                ans += 1
            cur = cur.next

        return ans