class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pq = []
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(pq, (lst.val, i))
        
        dummy = curr = ListNode(0)
        while pq:
            n = heapq.heappop(pq)
            cur_node = lists[n[1]]
            curr.next = cur_node
            curr = curr.next
            next_node = cur_node.next
            if next_node:
                heapq.heappush(pq, (next_node.val, n[1]))
            lists[n[1]] = lists[n[1]].next
            
                
        return dummy.next    