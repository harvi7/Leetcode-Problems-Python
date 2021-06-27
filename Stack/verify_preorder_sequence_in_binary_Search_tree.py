class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        lastPopped = float("-inf")
        
        for x in preorder:
            if lastPopped > x: return False
            while stack and x > stack[-1]: lastPopped = stack.pop()
            stack.append(x)
        return True