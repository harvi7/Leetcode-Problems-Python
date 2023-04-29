class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        listLength = 0
        frontNode, endNode = None, None
        currentNode = head

        while currentNode:
            listLength += 1
            if endNode:
                endNode = endNode.next

            if listLength == k:
                frontNode = currentNode
                endNode = head

            currentNode = currentNode.next

        frontNode.val, endNode.val = endNode.val, frontNode.val 
        return head