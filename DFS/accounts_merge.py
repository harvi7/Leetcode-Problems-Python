# https://leetcode.com/problems/accounts-merge/discuss/489526/Python-UnionFindDFS-two-solutions
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_name = {}
        graph = collections.defaultdict(list)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[email].append(acc[1])
                graph[acc[1]].append(email)
                email_name[email] = name
                
        seen = set()
        res = []
        for email in email_name.keys():
            if email not in seen:
                current_group = []
                self.DFS(email, current_group, seen, graph)
                res.append([email_name[email]]+sorted(current_group))
        return res
    
    def DFS(self, current, current_group, seen, graph):
        seen.add(current)
        current_group += [current]
        for nxt in graph[current]:
            if nxt not in seen:
                self.DFS(nxt, current_group, seen, graph)
        return