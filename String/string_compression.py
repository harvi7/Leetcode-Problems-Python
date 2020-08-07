class Solution:
    def compress(self, chars: List[str]) -> int:
        index, i = 0, 0
        while i < len(chars) :
            j = i
            while j < len(chars) and chars[j] == chars[i]:
                j += 1
            chars[index] = chars[i]
            index += 1
            if j - i > 1:
                for c in str(j -i):
                    chars[index] = c
                    index += 1
            i = j
        return index