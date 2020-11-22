class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)
        if not words or n == 0: return True

        for i in range(n):
            for j in range(len(words[i])):
                if j >= n or len(words[j]) <= i or words[j][i] != words[i][j]:
                    return False

        return True