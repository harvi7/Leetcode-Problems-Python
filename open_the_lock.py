# https://leetcode.com/problems/open-the-lock/discuss/110232/Accepted-PythonJava-BFS-%2B-how-to-avoid-TLE

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if target in visited:
            return -1
        queue = collections.deque(['0000'])
        level  = -1
        
        while queue:
            size = len(queue)
            level += 1
            for _ in range(size):
                node = queue.popleft()
                if node == target: return level
                if node in visited: continue
                visited.add(node)
                queue.extend(self.successors(node))
        return -1

    def successors(self, src):
            res = []
            for i, ch in enumerate(src):
                num = int(ch)
                res.append(src[:i] + str((num - 1) % 10) + src[i+1:])
                res.append(src[:i] + str((num + 1) % 10) + src[i+1:])
            return res