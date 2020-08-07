class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def getNextPosition(nums, index, ifForward):
            direction = nums[index] >= 0
            if direction != ifForward:
                return -1
            nextIndex = (index + nums[index]) % len(nums)
            if nextIndex < 0:
                nextIndex = nextIndex + len(nums)
            if nextIndex == index: return -1
            return nextIndex
        
        if len(nums) <= 1:
            return False    
        for i in range(len(nums)):
            slow = fast = i
            ifForward = nums[i] > 0
            while True:
                slow = getNextPosition(nums, slow, ifForward)
                if slow == -1: break
                fast = getNextPosition(nums, fast, ifForward)
                if fast == -1: break
                fast = getNextPosition(nums, fast, ifForward)
                if fast == -1: break
                if slow == fast: return True  
        return False
    