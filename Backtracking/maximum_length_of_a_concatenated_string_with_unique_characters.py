class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.res = 0
        self.dfs(arr, 0, "", self.res)
        return self.res

    def dfs(self, arr, idx, s, res):
        if self.unique(s):
            self.res = max(self.res, len(s))
        else:
            return
        for i in range(idx, len(arr)):
            if self.unique(arr[i]):
                self.dfs(arr, i + 1, s + arr[i], res)
                
    def unique(self, s):
        counter = Counter(s)
        for letter , freq in counter.items():
            if freq > 1:
                return False
        return True