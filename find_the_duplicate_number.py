class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slowPointer = nums[0]
        fastPointer = nums[0]
        
        slowPointer = nums[slowPointer]
        fastPointer = nums[nums[fastPointer]]
        
        while slowPointer != fastPointer:
            slowPointer = nums[slowPointer]
            fastPointer = nums[nums[fastPointer]]
        
        aPointer = nums[0]
        bPointer = slowPointer
    
        while aPointer != bPointer:
            aPointer  = nums[aPointer]
            bPointer = nums[bPointer]

        return aPointer