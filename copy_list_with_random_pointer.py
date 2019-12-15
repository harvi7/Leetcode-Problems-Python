class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        curr = head
        next = None
       
        while curr:
          next = curr.next
          copy = Node(curr.val, None, None)
          curr.next = copy
          copy.next = next
          curr = next
        
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        curr = head

        dummy_head = Node(0, None, None)
        clone_list_tail = dummy_head
        copy = None

        while curr:
            next = curr.next.next
            copy = curr.next
            clone_list_tail.next = copy
            clone_list_tail = copy
            curr.next = next

            curr = next
        return dummy_head.next