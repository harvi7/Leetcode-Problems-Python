class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        ch = list(str(N))
        mark = len(ch)
        for i in range(mark - 1, 0, -1):
            if ch[i] < ch[i - 1]:
                mark = i - 1
                ch[i - 1] = str(int(ch[i - 1]) - 1)

        ch[mark + 1:] = '9' * (len(ch) - mark - 1)
        return int("".join(ch))