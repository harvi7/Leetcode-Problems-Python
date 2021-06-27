class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(idx, path):
            if len(path) == 4 or idx == len(s):
                if len(path) == 4 and idx == len(s):
                    output.append(".".join(path))
                return
            for i in range(idx, min(idx + 3, len(s))):
                ip = s[idx : i + 1]
                if i == idx or (i > idx and s[idx] != "0" and int(ip) < 256):
                    dfs(i + 1, path + [ip])
        
        output = []
        dfs(0, [])
        return output