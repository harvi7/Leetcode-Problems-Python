class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_log = []
        alpha_log = []
        for log in logs:
            
            if log.split(" ")[1].isdigit():
                digit_log.append(log)
            else:
                alpha_log.append(log)
            
        return sorted(alpha_log, key = lambda x : [x.split(" ")[1:], x[0]]) + digit_log