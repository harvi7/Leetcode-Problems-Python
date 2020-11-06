class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        currentNode, lastMNode= head, head
        while currentNode:
            mCount, nCount = m, n
            while currentNode and mCount != 0:
                lastMNode = currentNode
                currentNode = currentNode.next
                mCount -= 1
            
            while currentNode and nCount != 0:
                currentNode = currentNode.next
                nCount -= 1
            
            lastMNode.next = currentNode
        
        return head