class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        values, current = [], head
        while current:
            values.append(current.val)
            current = current.next
        
        result, stack = [0] * len(values), []
        for i in range(len(values) - 1, -1, -1):
            while stack and stack[-1] <= values[i]:
                stack.pop()
            if len(stack) != 0:
                result[i] = stack[-1]
            stack.append(values[i])
            
        del stack
        return result