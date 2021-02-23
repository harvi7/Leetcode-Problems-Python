class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        return self.helper(nestedList, 1)
    
    def helper(self, nestedList, depth):
        s = 0;
        for n in nestedList:
            if n.isInteger():
                s += n.getInteger() * depth
            else:
                s += self.helper(n.getList(), depth + 1)
        return s