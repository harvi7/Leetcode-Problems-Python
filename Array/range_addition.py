class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * length
        
        for update in updates:
            value, start, end = update[2], update[0], update[1]
            res[start] += value
            if end < length - 1:
                res[end + 1] -= value

        sum = 0;
        for i in range(length):
            sum += res[i]
            res[i] = sum
        return res