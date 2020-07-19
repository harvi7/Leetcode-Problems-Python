class Solution:
    def toGoatLatin(self, S: str) -> str:
        s = S.split()
        result = ''
        for i, w in enumerate(s):
            if re.match(r'(?i)^[aeiou]', w):
                result += w + 'ma' + (i + 1) * 'a' + ' '
            else:
                result += w[1:] + w[0] + 'ma' + (i + 1) * 'a' + ' '

        return result.strip()