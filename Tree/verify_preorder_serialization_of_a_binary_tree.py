class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        
        prev = None  
        for ch in preorder:
            if ch == ',': 
                slots -= 1
                if slots < 0:
                    return False

                if prev != '#':
                    slots += 2
            prev = ch
        
        slots = slots + 1 if ch != '#' else slots - 1 

        return slots == 0