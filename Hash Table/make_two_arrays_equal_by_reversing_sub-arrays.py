class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        _map = {}
        for t in target:
            _map[t] = _map.get(t, 0) + 1
        
        for a in arr:
            if a in _map and _map.get(a) > 0:
                _map[a] = _map[a] - 1
            else: return False
        return True