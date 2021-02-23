import collections

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        children = collections.defaultdict(list)
        for c, p in zip(pid, ppid): 
            children[p].append(c)
        queue = [kill]
        for processToKill in queue: 
            queue.extend(children.get(processToKill, []))
        return queue